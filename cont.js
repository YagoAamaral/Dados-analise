const puppeteer = require("puppeteer-extra");
const stealth = require("puppeteer-extra-plugin-stealth");

puppeteer.use(stealth());

(async () => {
    const readline = require("readline").createInterface({
        input: process.stdin,
        output: process.stdout
    });

    readline.question("Digite o dominio que você quer verificar: ", async (userInput) => {
        const browser = await puppeteer.launch({
            headless: true,
            args: [
                '--disable-gpu',
                '--no-sandbox',
                '--disable-setuid-sandbox',
                '--disable-infobars',
                '--window-size=1200,800'
            ]
        });

        const page = await browser.newPage();
        await page.setViewport({ height: 780, width: 600 });

        const targetURL = "https://verificaemail.com.br/";
        await page.goto(targetURL, { waitUntil: 'load', timeout: 0 });

        try {
           
            await page.waitForSelector("textarea[name='email_list']", { timeout: 60000 });
            await page.type("textarea[name='email_list']", userInput);

            
            await page.click("#btn_check_emails"); 
            await page.waitForNavigation();

            
            const results = await page.evaluate(() => {
                const tds = Array.from(document.querySelectorAll("table td"));
                return tds.map(td => td.innerText);
            });

            console.log("Resultados extraídos:", results);
        } catch (error) {
            console.error("Erro ao buscar dados:", error);
        }

        await browser.close();
        readline.close();
    });
})();
