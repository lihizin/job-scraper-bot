import sqlite3

# Connect to the database
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor() # send sql commands to the db, reading results from queries

# List of websites to add (name, url)
websites = [
    ("Google", "https://www.google.com/about/careers/applications/jobs/results?location=Israel"),
    ("Wix", "https://careers.wix.com/positions?locations=tel-aviv%2Cbeer-sheva"),
    ("monday.com", "https://monday.com/careers?location=telaviv"),
    ("Refael", "https://career.rafael.co.il/"),
    ("Elbit", "https://elbitsystemscareer.com/go/%D7%94%D7%A0%D7%93%D7%A1%D7%94-%D7%95%D7%A4%D7%99%D7%AA%D7%95%D7%97/9358855/"),
    ("Mize", "https://mize.tech/careers/"),
    ("Uveye","https://www.uveye.com/careers/"),
    ("Verint", "https://fa-epcb-saasfaprod1.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX/jobs?location=Israel"),
    ("CheckPoint", "https://careers.checkpoint.com/index.php?q=&module=cpcareers&a=search&fa%5B%5D=country_ss%3AIsrael&sort="),
    ("Thetaray", "https://www.comeet.com/jobs/thetaray/72.00F"),
    ("Earnix", "https://earnix.com/careers-search/?j=&f=%5B%7B%22type%22%3A%22Location%22%2C%22item%22%3A%22Ramat%20Gan%2C%20Israel%22%7D%5D"),
    ("Inmanage", "https://www.inmanage.co.il/%D7%93%D7%A8%D7%95%D7%A9%D7%99%D7%9D"),
    ("Atera", "https://www.atera.com/careers/"),
    ("abra", "https://www.abra-it.com/en/career/"),
    ("eternitech", "https://eternitech.com/jobs/"),
    ("Mend.io", "https://www.mend.io/careers/#positions"),
    ("Zadara", "https://jobs.lever.co/Zadara?location=Tel%20Aviv"),
    ("BMC", "https://jobs.bmc.com/Careers/SearchJobs/?listFilterMode=1&1274=9409&1274_format=1347&intcmp=JobsByCountry"),
    ("VAST", "https://www.vastdata.com/careers#open-positions"),
    ("Cybereason", "https://www.cybereason.com/careers/all-jobs"),
    ("SimilarWeb", "https://www.similarweb.com/corp/careers/#opportunities"),
    ("WalkMe", "https://www.walkme.com/careers/careers_list/"),
    ("Armis", "https://www.armis.com/armis-careers/#discoverjobs"),
    ("Next Insurance", "https://www.nextinsurance.com/careers/#careers"),
    ("Orca Security", "http://orca.security/about/careers/#open-positions"),
    ("Salt Security", "https://salt.security/job-board"),
    ("WSC Sports", "https://wsc-sports.com/careers/"),
    ("Aquant", "https://www.aquant.io/careers/"),
    ("Fundbox", "https://fundbox.com/careers/"),
    ("Melio", "https://careers.meliopayments.com/"),
    ("Tytocare", "https://www.tytocare.com/careers/#openPositionSection"),
    ("Lightricks", "https://careers.lightricks.com/careers?query=&office=Jerusalem&department=all"),
    ("Lightricks", "https://careers.lightricks.com/careers?query=&office=Haifa&department=all"),
    ("Taboola", "https://www.taboola.com/careers/jobs#team=&location=23621"),
    ("Outbrain", "https://www.outbrain.com/careers/"),
    ("Lemonade", "https://makers.lemonade.com/"),
    ("HoneyBook", "https://www.honeybook.com/careers"),
    ("Viber", "https://www.viber.com/en/careers-israel/"),
    ("Kaltura", "https://corp.kaltura.com/company/careers/"),
    ("Tipalti", "https://tipalti.com/company/jobs/"),
    ("BioCatch", "https://www.biocatch.com/cybersecurity-careers"),
    ("Playtika", "https://www.playtika.com/careers/research-development/"),
    ("Playtika", "https://www.playtika.com/careers/analytics/"),
    ("Playtika", "https://www.playtika.com/careers/data-ai/"),
    ("Playtika", "https://www.playtika.com/careers/qa/"),
    ("Playtika", "https://www.playtika.com/careers/security-it/"),
    ("Forter", "https://www.forter.com/job-opportunities/"),
    ("Rapyd", "https://www.rapyd.net/company/careers-search/?location=israel"),
    ("Flytrex", "https://www.flytrex.com/careers/"),
    ("Bringg", "https://www.bringg.com/company/careers/"),
    ("Via", "https://ridewithvia.com/careers/jobs"),
    ("Buildots", "https://www.buildots.com/careers/"),
    ("Optibus", "https://optibus.com/company/careers/jobs/"),
    ("Cloudinary", "https://cloudinary.com/careers/jobs"),
    ("RapidAPI", "https://rapidapi.com/company/careers/#join"),
    ("Sisense", "https://www.sisense.com/about/careers/#job-positions-table"),
    ("Papaya Global", "https://www.papayaglobal.com/careers/"),
    ("AppsFlyer", "https://careers.appsflyer.com/#careersOps"),
    ("IronSource", "https://unity.com/careers/positions?location=tel-aviv"),
    ("Riskified", "https://www.riskified.com/careers/#positions"),
    ("Weka", "https://www.weka.io/company/careers/#career-position"),
    ("Cheq", "https://www.cheq.ai/careers"),
    ("PlainID", "https://www.plainid.com/work-with-us/"),
    ("Pipl", "https://www.comeet.com/jobs/pipl/22.008"),
    ("Syqe Medical", "https://syqe.com/careers/"),
    ("Fabric", "https://getfabric.com/careers"),
    ("Scopio Labs", "https://scopiolabs.com/careers/?utm_term=scopio%20digital%20morphology&utm_campaign=Search+All-in+28/5&utm_source=adwords&utm_medium=ppc&hsa_acc=3374207472&hsa_cam=22614349834&hsa_grp=177107399461&hsa_ad=754951383067&hsa_src=g&hsa_tgt=kwd-2423818567330&hsa_kw=scopio%20digital%20morphology&hsa_mt=b&hsa_net=adwords&hsa_ver=3&gad_source=1&gad_campaignid=22614349834&gbraid=0AAAAA-GPCAupAhurLnE9-JhwivL6REiDB&gclid=CjwKCAjw6ZTCBhBOEiwAqfwJd5TR5TDCz62Wh39g69UhngR0L_zCenQ45G3xefpiWC9aQ-ycSD0rdRoC5eAQAvD_BwE"),
    ("Remilk", "https://www.remilk.com/careers"),
    ("Upstream Security", "https://www.upstream.auto/careers/"),
    ("Verbit", "https://verbit.ai/careers-listing/"),
    ("Jfrog", "https://join.jfrog.com/positions/?gh_office=25868"),
    ("Nvidia", "https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite?locationHierarchy1=2fcb99c455831013ea52bbe14cf9326c"),
    ("Cato Networks", "https://www.catonetworks.com/careers/?location=Israel%3B+Tel+Aviv+District%2C+Israel"),
    ("intenthq", "https://intenthq.teamtailor.com/jobs"),
    ("Cellebrite", "https://cellebrite.com/en/about/careers/positions/?comeet_cat=israel&comeet_all=all"),
    ("Hailo", "https://hailo.ai/company-overview/careers/"),
    ("Bizzabo", "https://www.bizzabo.com/careers#openings"),
    ("Vayyar", "https://vayyar.com/careers/#jobs"),
    ("Vanti", "https://tray.ai/careers"),
    ("Wiliot", "https://www.wiliot.com/careers"),
    ("Trigo", "https://www.trigoretail.com/careers/"),
    ("Lightico", "https://www.lightico.com/careers/"),
    ("Voyantis", "https://www.voyantis.ai/careers#positions"),
    ("C2A Security", "https://www.c2a-sec.com/careers/"),
    ("Hibob", "https://www.hibob.com/careers/"),
    ("Lusha", "https://www.lusha.com/careers/#careers"),
    ("OpenWeb", "https://www.openweb.com/careers/#join"),
    ("Mine", "https://mine.breezy.hr/"),
    ("AccessiBe", "https://www.comeet.com/jobs/accessibe/D5.00B"),
    ("Jiga", "https://www.ycombinator.com/companies/jiga/jobs/"),
    ("Varos", "https://www.ycombinator.com/companies/varos"),
    ("Diversion", "https://www.ycombinator.com/companies/diversion/jobs"),
    ("Vimeo", "https://vimeo.com/careers/openings"),
    ("Pendo", "https://job-boards.greenhouse.io/pendo"),
    ("Unity", "https://unity.com/careers/positions"),
    ("Vonage", "https://www.vonage.com/careers/search/#loc=4010269002&dept=0&page=1&sort=desc"),
    ("Vonage", "https://www.vonage.com/careers/search/#loc=4059245002&dept=0&page=1&sort=desc"),
    ("ZoomInfo", "https://www.zoominfo.com/about/careers"),
    ("Datadog", "https://careers.datadoghq.com/engineering/?location_EMEA%5B0%5D=Israel"),
    ("Datadog", "https://careers.datadoghq.com/engineering/?location_EMEA%5B0%5D=Israel"),
    ("Rubrik", "https://www.rubrik.com/company/careers"),
    ("MongoDB", "https://www.mongodb.com/company/careers/teams/engineering"),
    ("MongoDB", "https://www.mongodb.com/company/careers/teams/product-management-and-design"),
    ("Microsoft", "https://jobs.careers.microsoft.com/global/en/search?lc=Israel&pg=1&pgSz=20&o=Relevance&flt=true&l=en_us"),
    ("Intuit", "https://www.intuit.com/careers/locations/israel/#jobs"),
    ("JPMorgan Chase", "https://www.intuit.com/careers/locations/israel/#jobsv"),
    ("IBM", "https://www.ibm.com/planetwide/il/"),
    ("Apple", "https://www.apple.com/careers/il/teams/software-and-services.html"),
    ("Apple", "https://www.apple.com/careers/il/teams/machine-learning-and-ai.html"),
    ("Facebook", "https://www.metacareers.com/jobs?offices[0]=Tel%20Aviv%2C%20Israel"),
    ("Oracle", "https://careers.oracle.com/en/sites/jobsearch/jobs?location=Israel&locationId=300000000106941&locationLevel=country&mode=location"),
    ("Salesforce", "https://careers.salesforce.com/en/jobs/?search=&country=Israel&pagesize=20#results"),
    ("Cisco", "https://jobs.cisco.com/jobs/SearchJobs/?21178=%5B102692%5D&21178_format=6020&listFilterMode=1"),
    ("Intel", "https://intel.wd1.myworkdayjobs.com/External?locations=1e4a4eb3adf101aaeda8a474bf818ecd&locations=1e4a4eb3adf101f41cd29774bf8184cd&locations=1e4a4eb3adf1013563ba9174bf817fcd"),
    ("SAP", "https://jobs.sap.com/search/?createNewAlert=false&q=&locationsearch=israel&optionsFacetsDD_department=&optionsFacetsDD_customfield3=&optionsFacetsDD_country="),
    ("Dell", "https://jobs.dell.com/en/location/israel-jobs/375/294640/2"),
    ("HP", "https://apply.hp.com/careers?query=israel&domain=hp.com"),
    ("Samsung", "https://sec.wd3.myworkdayjobs.com/Samsung_Careers?locations=189767dd6c92013c2fa62e7fa5291272"),
    ("Sony", "https://www.sony.net/SonyInfo/Careers/"),
    ("Qualcomm", "https://careers.qualcomm.com/careers?location=Ramat%20Gan%2C%20Israel&pid=446703459646&domain=qualcomm.com&sort_by=relevance"),
    ("Qualcomm", "https://careers.qualcomm.com/careers?location=Jerusalem%2C%20Jerusalem%20District%2C%20Israel&pid=446703459646&domain=qualcomm.com&sort_by=relevance"),
    ("Qualcomm", "https://careers.qualcomm.com/careers?location=Hod%20Hasharon%2C%20Haifa%20District%2C%20Israel&pid=446704043461&domain=qualcomm.com&sort_by=relevance"),
    ("Broadcom", "https://broadcom.wd1.myworkdayjobs.com/External_Career?locations=2314daa817fc016cb4c254532e010de8"),
    ("Texas Instruments", "https://careers.ti.com/en/sites/CX/jobs?mode=location"),
    ("Marvell", "https://marvell.wd1.myworkdayjobs.com/MarvellCareers?Country=084562884af243748dad7c84c304d89a"),
    ("Skyworks", "https://www.skyworksinc.com/en/Careers"),
    ("Altera", "https://altera.wd1.myworkdayjobs.com/Altera"),
    ("Motoroll", "https://motorolasolutions.wd5.myworkdayjobs.com/Careers?locationCountry=084562884af243748dad7c84c304d89a"),
    ("CheckMarx!", "https://checkmarx.com/company/careers/#jobs-table"),
    ("Vronis", "https://careers.varonis.com/"),
    ("Drivenets", "https://drivenets.com/careers/"),
    ("Tricentis", "https://tricentis.wd1.myworkdayjobs.com/Tricentis_Careers?locations=01dd50ae597b1000b3fbd055e9f00000"),
    ("Amazon", "https://www.amazon.jobs/en/search?base_query=&loc_query=Israel&country=ISR"),
    ("Overwolf", "https://careers.overwolf.com/#position"),
    ("ReasonLabs","https://reasonlabs.com/career"),
    ("Clarative","https://careers.clarivate.com/search-results"),
    ("Mobileye", "https://careers.mobileye.com/jobs"),
    ("Zenity", "https://zenity.io/careers#job-openings"),
    ("Applied Materials", "https://careers.appliedmaterials.com/careers?location=Rehovot%2C%20Center%20District%2C%20Israel&pid=790303217423&Country=Israel&domain=appliedmaterials.com&sort_by=relevance&triggerGoButton=false&triggerGoButton=true"),
    ("Equalweb", "https://www.equalweb.com/10393/11527/careers"),
    ("Mastercard","https://careers.mastercard.com/us/en/search-results"),
    ("Final", "https://www.final.co.il/career/"),
    ("QuickLizard", "https://quicklizard.com/careers/#positions"),
    ("Qualitest", "https://careers.qualitestgroup.com/search/?searchby=location&createNewAlert=false&q=&locationsearch=israel&geolocation=&optionsFacetsDD_country=&optionsFacetsDD_city="),
    ("Emerson", "https://hdjq.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/jobs?location=Israel&locationId=300000000228780&locationLevel=country&mode=location"),
    ("Scodix","https://scodix.com/company/careers/"),
    ("wsc-sports", "https://wsc-sports.com/careers/"),
    ("Cyberark", "https://www.cyberark.com/careers/all-job-openings/"),
    ("Upwind", "https://www.upwind.io/careers"),
    ("midrag", "https://careers.topmatch.co.il/midrag/index.html"),
    ("Optimove","https://www.optimove.com/careers#location=Israel"),
    ("Radcom", "https://radcom.com/careers/"),
    ("Parallel Wireless", "https://jobs.lever.co/parallelwireless?location=Israel"),
    ("Playstudio", "https://www.comeet.com/jobs/playstudios/E2.00B"),
    ("Morphisec", "https://www.morphisec.com/careers/#open-positions"),
    ("MDclone", "https://www.comeet.com/jobs/mdclone/66.004"),
    ("DRS RADA","https://www.drsrada.com/careers"),
    ("audiocodes","https://www.audiocodes.com/careers/positions?countryGroup=Israel"),
    ("Ribbon", "https://vhr-genband.wd1.myworkdayjobs.com/ribboncareers?locationCountry=084562884af243748dad7c84c304d89a"),
    ("pwc", "https://www.pwc.com/gx/en/careers/student-job-results.html?wdcountry=ISR&wdjobsite=Global_Campus_Careers&flds=jobreqid,title,location,los,specialism,grade,industry,region,apply,jobsite,iso"),
    ("capow", "https://capow.energy/careers/"),
    ("SivanDesign", "https://sivandesign.com/company/careers/"),
    ("Webtech innovation", "https://www.webtech-inv.co.il/careers"),
    ("Adtran", "https://adtran.wd3.myworkdayjobs.com/ADTRAN?locations=636f8af17f1001d1a13368850f01c280&locations=636f8af17f10016a4a9842850f014c80"),
    ("Trego", "https://www.trego.co.il/company/careers/"),
    ("Siemens", "https://jobs.siemens.com/careers?location=Israel&pid=563156124731547&domain=siemens.com&sort_by=relevance&utm_source=j_c_global&triggerGoButton=false"),
    ("Fiverr", "https://www.fiverr.com/jobs/teams?location=tlv"),
    ("Go4it", "https://www.go4-it.co.il/go4it-jobs-1"),
    ("ICE", "https://careers.ice.com/jobs?country=Israel&page=1")

]

# Insert them into the database
for name, url in websites:
    cursor.execute("INSERT INTO websites (name, url) VALUES (?, ?)", (name, url))

# Save and close
conn.commit()
conn.close()

print("Websites added successfully.")
