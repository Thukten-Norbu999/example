import puppeteer from "puppeteer"


const INDEX_SEL = "input#indexno"
const DOB_SEL = "input#dob[type='date']"
const DOB = "07/01/2004"

async function init() {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto("https://bcsea.site/result2021");
  
    // Set screen size
    await page.setViewport({ width: 1080, height: 1024 });
    console.log(page.url());
  
    return { browser, page };
  }

async function getRightIndex(page, idx_no, dob_){
    console.log("getRightIndex function")
    await page.waitForSelector(INDEX_SEL);
    const index = await page.$(INDEX_SEL)

    const dob = await page.$(DOB_SEL)
    await index.type(idx_no)
    await dob.type(dob_)
    await page.click("button[type='submit']");
    

    try{
        const result = await page.waitForSelector("#myTable")
        if(result){
            return index
        }
        else{
            return "Wrong"
        }
    }

    catch(error){
        console.log("error", error)
    }       
    
}

async function main(){
    const {browser, page} = await init()
    let run = true
    let ind = 12241400631
    while(run){
        
        const val = getRightIndex(page, ind, DOB)
        if(val!=="Wrong"){
            run = false
        }
        else{
            console.log(`right index no is ${ind}`)
        }
        i++
    }
}

main()