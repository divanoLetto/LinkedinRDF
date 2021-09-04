from linkedin_scraper import actions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from parsel import Selector

from Experience import Experience, WorkingExperience, EducationExperience
from Member import MyPerson, Company, School, global_companies, global_schools
from Skill import Skill
from utlis import xstr, splitDate

driver = webdriver.Chrome("C:/Users/Computer/Desktop/chromedriver/92_0_4515_131/chromedriver.exe")

# Company web scraping function
def search_company(company_id, company_url, company_name):
    company_about, company_website, company_phone, company_industry = None, None, None, None
    company_headquarters, company_type, company_founded, company_speciality, company_size = None, None, None, None, None

    if company_url and len(company_url) > 0:
        # apro la pagina dell'azienda in una nuova finestra
        company_url = 'https://www.linkedin.com' + xstr(company_url)
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(company_url)
        sleep(2)
        # if company_url.split("/")[-2] != "about":
        #    company_url = company_url + "about/"
        if driver.current_url.split("/")[-2] != "about":
            company_url = driver.current_url + "about/"
        driver.get(company_url)
        sleep(2)
        # se la pagina è non disponibile su linkedin
        if driver.current_url.split("/")[-2] == "unavailable":
            driver.close()
            sleep(2)
            driver.switch_to.window(driver.window_handles[0])
        else:
            new_sel = Selector(text=driver.page_source)
            main_prop_section = new_sel.xpath('//div[@class="ember-view"]//section[contains(@class,"artdeco-card p4 mb3")]')[0]
            company_about = main_prop_section.xpath('.//p[contains(@class, "break-words white-space-pre-wrap")]')[
                0].root.text
            key, value = "", ""
            first_dt = True
            first_dd = True
            dict_properties = {}
            company_list_properties = driver.find_elements_by_xpath(
                './/dt[contains(@class, "org-page-details__definition-term")] | .//dd')
            for comp_prop in company_list_properties:
                outerhtml = comp_prop.get_attribute('outerHTML')  # to extract outerHTML
                tag_value = outerhtml.split(' ')[0]  # to extract first word
                if tag_value == "<dt":
                    if first_dt:
                        first_dt = False
                    else:
                        dict_properties[key] = value
                        key = ""
                        value = ""
                        first_dd = True
                    key = key + comp_prop.text
                elif tag_value == "<dd":
                    if first_dd is True:
                        value = comp_prop.text
                        first_dd = False
            dict_properties[key] = value
            if "Website" or "Sito Web" in dict_properties.keys():
                if "Website" in dict_properties.keys():
                    company_website = dict_properties["Website"]
                if "Sito Web" in dict_properties.keys():
                    company_website = dict_properties["Sito Web"]
            if "Phone" or "Telefono" in dict_properties.keys():
                if "Phone" in dict_properties.keys():
                    company_phone = dict_properties["Phone"]
                if "Telefono" in dict_properties.keys():
                    company_phone = dict_properties["Telefono"]
            if "Industry" or "Settore" in dict_properties.keys():
                if "Industry" in dict_properties.keys():
                    company_industry = dict_properties["Industry"]
                if "Settore" in dict_properties.keys():
                    company_industry = dict_properties["Settore"]
            if "Company size" or "Dimensioni dell'azienda" in dict_properties.keys():
                if "Company size" in dict_properties.keys():
                    company_size = dict_properties["Company size"]
                if "Dimensioni dell’azienda" in dict_properties.keys():
                    company_size = dict_properties["Dimensioni dell’azienda"]
            if "Headquarters" or "Sede principale" in dict_properties.keys():
                if "Headquarters" in dict_properties.keys():
                    company_headquarters = dict_properties["Headquarters"]
                if "Sede principale" in dict_properties.keys():
                    company_headquarters = dict_properties["Sede principale"]
            if "Type" or "Tipo" in dict_properties.keys():
                if "Type" in dict_properties.keys():
                    company_type = dict_properties["Type"]
                if "Tipo" in dict_properties.keys():
                    company_type = dict_properties["Tipo"]
            if "Founded" or "Data di fondazione" in dict_properties.keys():
                if "Founded" in dict_properties.keys():
                    company_founded = dict_properties["Founded"]
                if "Data di fondazione" in dict_properties.keys():
                    company_founded = dict_properties["Data di fondazione"]
            if "Specialities" or "Settori di competenza" in dict_properties.keys():
                if "Specialities" in dict_properties.keys():
                    company_speciality = dict_properties["Specialities"]
                if "Settori di competenza" in dict_properties.keys():
                    company_speciality = dict_properties["Settori di competenza"]
            driver.close()
            sleep(3)
            driver.switch_to.window(driver.window_handles[0])
    this_company = Company(id=company_id, url=company_url, about=company_about, place_name=company_name,
                           website=company_website, phone=company_phone, industry=company_industry,
                           companySize=company_size, headquarter=company_headquarters, type=company_type,
                           founded=company_founded, speciality=company_speciality)
    return this_company

# School web scraping function
def search_school(school_id, school_url, school_name):
    school_about, school_website, school_phone, school_industry = None, None, None, None
    school_headquarters, school_type, school_founded, school_speciality, school_size = None, None, None, None, None

    if school_url and len(school_url) > 0:
        school_url = 'https://www.linkedin.com' + xstr(school_url)
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(school_url)
        sleep(2)
        if driver.current_url.split("/")[-2] != "about":
            school_url = driver.current_url + "about/"
        driver.get(school_url)
        if driver.current_url.split("/")[-2] == "unavailable":
            driver.close()
            sleep(2)
            driver.switch_to.window(driver.window_handles[0])
        else:
            new_sel = Selector(text=driver.page_source)
            main_prop_section = \
                new_sel.xpath('//div[@class="ember-view"]//section[contains(@class,"artdeco-card p4 mb3")]')[0]
            school_about = main_prop_section.xpath('.//p[contains(@class, "break-words white-space-pre-wrap")]')[
                0].root.text
            key = ""
            value = ""
            first = True
            dict_properties = {}
            school_list_properties = driver.find_elements_by_xpath(
                './/dt[contains(@class, "org-page-details__definition-term")] | .//dd')
            for school_prop in school_list_properties:
                outerhtml = school_prop.get_attribute('outerHTML')
                tag_value = outerhtml.split(' ')[0]
                if tag_value == "<dt":
                    if first:
                        first = False
                    else:
                        dict_properties[key] = value
                        key = ""
                        value = ""
                    key = key + school_prop.text
                elif tag_value == "<dd":
                    value = value + school_prop.text + " "
            dict_properties[key] = value
            if "Sito Web" in dict_properties.keys():
                company_website = dict_properties["Sito Web"]
            if "Telefono" in dict_properties.keys():
                company_phone = dict_properties["Telefono"]
            if "Settore" in dict_properties.keys():
                company_industry = dict_properties["Settore"]
            if "Dimensioni dell'azienda" in dict_properties.keys():
                company_size = dict_properties["Dimensioni dell’azienda"]
            if "Sede principale" in dict_properties.keys():
                company_headquarters = dict_properties["Sede principale"]
            if "Tipo" in dict_properties.keys():
                company_type = dict_properties["Tipo"]
            if "Data di fondazione" in dict_properties.keys():
                company_founded = dict_properties["Data di fondazione"]
            if "Settori di competenza" in dict_properties.keys():
                company_speciality = dict_properties["Settori di competenza"]
            driver.close()
            sleep(3)
            driver.switch_to.window(driver.window_handles[0])

    this_school = School(id=school_id, url=school_url, about=school_about, place_name=school_name,
                         website=school_website, phone=school_phone, industry=school_industry,
                         companySize=school_size, headquarter=school_headquarters, type=school_type,
                         founded=school_founded, speciality=school_speciality)
    return this_school


# Inizializing web browser
email = "bryansevendeadlysins@outlook.com"
password = "Arthur123"
actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
sleep(27.5)
driver.get('https:www.google.com')
search_query = driver.find_element_by_name('q')
accept_button = driver.find_element_by_id('L2AGLb').click()
search_query.send_keys('site:linkedin.com/in/ AND "python developer" AND Firenze')  # send_keys() to simulate the search text key strokes
sleep(1)
search_query.send_keys(Keys.RETURN)  # .send_keys() to simulate the return key
sleep(1.5)

linkedin_urls = driver.find_elements_by_xpath("//div[contains(@class, 'tF2Cxc')]//div[contains(@class, 'yuRUbf')]")
linkedin_urls = [l.find_elements_by_xpath(".//*[@href]")[0] for l in linkedin_urls]
linkedin_urls = [elem.get_attribute('href') for elem in linkedin_urls]
sleep(1)

person_id = 0
wrk_exp_id = 0
edu_exp_id = 0
company_id = 0
school_id = 0
skill_id = 0

first = True
# Inizializing linkedin page views
for link in linkedin_urls:

    driver.get(link)
    sleep(1)
    # Arriva in fondo alla pagina e la scorre per far caricare tutte le informazioni
    lastHeight = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(1.5)
        newHeight = driver.execute_script("return document.body.scrollHeight")
        if newHeight == lastHeight:
            break
        lastHeight = newHeight
    to_scroll = 0
    while to_scroll<lastHeight:
        driver.execute_script("window.scrollTo(0, arguments[0]);", to_scroll)
        sleep(0.5)
        to_scroll = to_scroll + 100

    # Bottone da premere per visualizzare i contenuti aggiuntivi delle skills
    expand_experiences_btn = driver.find_element_by_xpath('//button[@aria-controls = "skill-categories-expanded"]')
    if expand_experiences_btn:
        driver.execute_script("arguments[0].click();", expand_experiences_btn)

    sleep(1.5)
    sel = Selector(text=driver.page_source)

    # Person web scraping section
    name = sel.xpath('//h1/text()').extract_first()
    if name:
        name = name.strip()
        first_name = xstr(name).split()[0]
        second_name = xstr(name).split()[1]
    else:
        first_name = ""
        second_name = ""
    current_job_role = sel.xpath('//*[starts-with(@class, "text-body-medium")]/text()').extract_first()
    if current_job_role:
        current_job_role = current_job_role.strip()
    company = sel.xpath('//div[@aria-label = "Azienda attuale"]/text()').extract_first()
    if company:
        company = company.strip()
    last_education = sel.xpath('//div[@aria-label = "Formazione"]/text()').extract_first()
    if last_education:
        last_education = last_education.strip()
    location = sel.xpath('//*[starts-with(@class, "text-body-small")]/text()').extract_first()
    if location:
        location = location.strip()
    about = sel.xpath('//section[contains(@class,"pv-about-section")]/div/text()').extract_first()
    if about:
        about = about.strip()

    linkedin_url = driver.current_url
    this_person = MyPerson(id=person_id, url=linkedin_url, about=about, location=location, firstName=first_name, secondName=second_name)
    person_id = person_id + 1

    # Working experience web scraping section
    experiences = []
    experience_lis = sel.xpath('//li[contains(@class,"pv-entity__position-group-pager pv-profile-section__list-item ember-view")]')
    for ex_li in experience_lis:
        ex_role, ex_company, ex_period, ex_location = "", "", "", ""

        alternative_experience_divs = experience_lis.xpath('.//div[contains(@class,"pv-entity__company-summary-info")]')
        # Nel caso di lavori multipli a una singola azienda
        if len(alternative_experience_divs) > 0:
            for alt_ex_div in alternative_experience_divs:
                ex_company = alt_ex_div.xpath('.//h3/span')[1].root.text
                ex_duration = alt_ex_div.xpath('.//h4/span')[1].root.text
                ex_roles = ex_li.xpath('.//ul//li//h3//span')
                for r in ex_roles[1::2]:
                    ex_role = ex_role + xstr(r.root.text) + " "
                ex_place_span = ex_li.xpath('.//h4[contains(@class, "pv-entity__location")]/span')[1]
                if ex_place_span and len(ex_place_span) > 1:
                    ex_location = ex_place_span[1].root.text
        # Nel caso di un lavoro presso un'azienda
        else:
            title_h3 = ex_li.xpath('.//h3')
            if title_h3:
                ex_role = title_h3[0].root.text
            ex_company_p = ex_li.xpath('.//p')
            if ex_company_p and len(ex_company_p)>1:
                ex_company = ex_company_p[1].root.text
            ex_period_span = ex_li.xpath('.//h4/span')
            if ex_period_span and len(ex_period_span)>1:
                ex_period = ex_period_span[1].root.text
            ex_place_span = ex_li.xpath('.//h4[contains(@class, "pv-entity__location")]/span')
            if ex_place_span and len(ex_place_span)>1:
                ex_location = ex_place_span[1].root.text
        exp_start_date, exp_end_date = splitDate(ex_period)

        # Company web scraping
        company_url = ex_li.xpath('.//a[@data-control-name  = "background_details_company"]')
        if company_url and len(company_url)>0:
            company_url = company_url[0].attrib['href']
        this_company = search_company(company_id=company_id, company_url=company_url ,company_name=ex_company)
        company_id = company_id + 1

        this_wrk_experience = WorkingExperience(id=wrk_exp_id, role=ex_role, place=this_company, location=ex_location, start_date=exp_start_date, end_date=exp_end_date)
        wrk_exp_id = wrk_exp_id + 1
        experiences.append(this_wrk_experience)
        this_person.add_working_experience(this_wrk_experience)

    # Education experiences web scraping section
    educations = []
    educations_lis = sel.xpath('//li[contains(@class,"pv-profile-section__list-item pv-education-entity pv-profile-section__card-item ember-view")]')
    for ed_li in educations_lis:
        ed_name, ed_role, ed_period, ed_location = "", "", "", ""
        title_h3 = ed_li.xpath('.//h3')
        if title_h3:
            ed_name = title_h3[0].root.text
        ed_college_p = ed_li.xpath('.//p/span')
        if ed_college_p and len(ed_college_p) > 1:
            ed_role = ed_college_p[1].root.text
        ed_period_span = ed_li.xpath('.//p[contains(@class,"entity__dates")]/span/time')
        if ed_period_span:
            per = ""
            for p in ed_period_span:
                per = per + p.root.text + " "
            ed_period = per
        ed_location_span = ed_li.xpath('.//h4[contains(@class, "pv-entity__location")]/span')
        ed_start_date, ed_end_date = splitDate(ed_period)

        # Education web scraping
        school_url = ed_li.xpath('.//a[@data-control-name  = "background_details_school"]')
        if school_url and len(school_url)>0:
            school_url = school_url[0].attrib['href']
        else:
            school_url = None  # todo nel caso il link non sia presente è possibile estrarre qualche informazione dalla pagina del profilo utente
        this_school = search_school(school_id=school_id, school_name=ed_name, school_url=school_url)
        school_id = school_id + 1

        this_school_experience = EducationExperience(id=edu_exp_id, role=ed_role, place=this_school, location=ed_location,
                                                     start_date=ed_start_date, end_date=ed_end_date)
        edu_exp_id = edu_exp_id + 1
        educations.append(this_school_experience)
        this_person.add_education_experience(this_school_experience)

    # Skills web scraping
    skills_spans = sel.xpath('//span[contains(@class,"pv-skill-category-entity__name-text")]')
    skills_texts = [el.root.text for el in skills_spans]
    if len(skills_texts) > 0:
        skills_texts = [s.strip() for s in skills_texts]
    for s_text in skills_texts:
        skl = Skill(skill_id, s_text)
        skill_id = skill_id + 1
        this_person.add_skill(skl)

    # Interests web scraping
    interests_spans = sel.xpath('//span[contains(@class,"pv-entity__summary-title-text")]')
    interests_texts = [el.root.text for el in interests_spans]
    interest_links = sel.xpath('//section[contains(@class,"pv-interests-section")]//li//a')
    interests = []
    for interest in range(len(interests_texts)):
        interests.append([interests_texts[interest], interest_links[interest]])
    if len(interests_texts) > 0:
        for interest in interests:
            interest[0] = interest[0].strip()
            interest[1] = interest[1].attrib['href']
    for interest in interests:
        new_interest = None

        if "company" in interest[1]:
            new_interest = search_company(company_id=company_id, company_url=interest[1], company_name=interest[0])
            this_person.add_interest(new_interest)
            company_id = company_id + 1
        elif "school" in interest[1]:
            new_interest = search_school(school_id=school_id, school_url=interest[1], school_name=interest[0])
            this_person.add_interest(new_interest)
            school_id = school_id + 1
        elif "group" in interest[1]:
            next_implemetation = "Not implemented"
        elif "influencer" in interest[1]:
            next_implemetation = "Not implemented"

    print('\n')
    this_person.print_rdf_info()
    print()

driver.quit()


