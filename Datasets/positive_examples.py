import scrapy

class HeadingSpider(scrapy.Spider):
    name = "heading function"

    start_urls = [
"http://timesofindia.indiatimes.com//city/chennai/two-cops-suffer-fracture-in-accidents/articleshow/62319936.cms",
"http://timesofindia.indiatimes.com//city/rajkot/two-women-child-killed-in-accident/articleshow/62320008.cms",
"http://timesofindia.indiatimes.com//city/chandigarh/7-killed-in-two-accidents/articleshow/62318662.cms",
"http://timesofindia.indiatimes.com//city/vadodara/bus-accident-kills-two-sparks-furore/articleshow/62320910.cms",
"http://timesofindia.indiatimes.com//city/surat/nri-kin-die-as-car-crashes-into-parked-truck-on-nh-8/articleshow/62319344.cms",
"http://timesofindia.indiatimes.com//city/kolkata/five-of-family-killed-in-highway-crash/articleshow/62320896.cms",
"http://timesofindia.indiatimes.com//city/coimbatore/new-year-celebration-turns-fatal-as-3-youngsters-die-in-suv-crash/articleshow/62329936.cms",
"http://timesofindia.indiatimes.com//city/bengaluru/boy-12-killed-in-highway-crash/articleshow/62332167.cms",
"http://timesofindia.indiatimes.com//city/bengaluru/5-of-mandya-family-killed-in-accident/articleshow/62331845.cms",
"http://timesofindia.indiatimes.com//city/bhopal/hubby-goes-to-new-year-bash-woman-dies-in-accident/articleshow/62334003.cms",
"http://timesofindia.indiatimes.com//city/kolhapur/3-from-mum-killed-in-accident/articleshow/62343541.cms",
"http://timesofindia.indiatimes.com//city/coimbatore/2-killed-in-as-many-road-accidents/articleshow/62343938.cms",
"http://timesofindia.indiatimes.com//city/mangaluru/2-youths-killed-in-accident/articleshow/62371960.cms",
"http://timesofindia.indiatimes.com//city/goa/constable-dies-in-road-accident/articleshow/62357974.cms",
"http://timesofindia.indiatimes.com//city/hyderabad/class-10-boy-goes-on-secret-joyride-dies-in-car-crash/articleshow/62375748.cms",
"http://timesofindia.indiatimes.com//city/delhi/man-dies-after-car-crashes-due-to-fog/articleshow/62397665.cms",
"http://timesofindia.indiatimes.com//city/hyderabad/student-on-way-to-birthday-bash-dies-in-car-crash/articleshow/62436890.cms",
"http://timesofindia.indiatimes.com//city/ludhiana/tyre-burst-proves-fatal-for-hc-lawyer-familyhc-lawyer-2-others-die-in-car-truck-crash/articleshow/62465060.cms",
"http://timesofindia.indiatimes.com//city/hyderabad/basara-priest-dies-3-hurt-in-car-crash/articleshow/62492165.cms",
"http://timesofindia.indiatimes.com//city/bengaluru/mechanic-dies-as-truck-crashes-into-under-construction-metro-station/articleshow/62494729.cms",
"http://timesofindia.indiatimes.com//city/goa/woman-killed-in-accident-at-calangute/articleshow/62372588.cms",
"http://timesofindia.indiatimes.com//city/rajkot/six-killed-in-two-different-accidents/articleshow/62370540.cms",
"http://timesofindia.indiatimes.com//city/varanasi/boy-killed-in-accident-mob-sets-vehicle-afire-in-ballia/articleshow/62376894.cms",
"http://timesofindia.indiatimes.com//city/coimbatore/two-students-among-3-killed-in-accident/articleshow/62386822.cms",
"http://timesofindia.indiatimes.com//city/indore/dps-bus-accident-innocent-lives-lost-little-glasses-shoes-lie-strewn-on-road/articleshow/62389804.cms",
"http://timesofindia.indiatimes.com//city/pune/policeman-hit-by-accident-victim-after-offering-help/articleshow/62397652.cms",
"http://timesofindia.indiatimes.com//city/chennai/revenue-sinks-five-accidents-on-third-day-of-tn-bus-strike/articleshow/62398087.cms",
"http://timesofindia.indiatimes.com//city/delhi/four-powerlifting-players-killed-in-a-road-accident-due-to-fog-at-singhu-border/articleshow/62399304.cms",
"http://timesofindia.indiatimes.com//city/madurai/pilgrim-among-3-killed-in-accidents/articleshow/62397868.cms",
"http://timesofindia.indiatimes.com//city/chennai/2-die-in-accidents-stalin-eps-spar-over-bus-staff-stir/articleshow/62408407.cms",
"http://timesofindia.indiatimes.com//city/aurangabad/inebriated-cop-loses-pistol-with-10-live-rounds-in-accident/articleshow/62411329.cms",
"http://timesofindia.indiatimes.com//city/chennai/driver-detained-in-fatal-accident-near-santhome-church/articleshow/62421144.cms",
"http://timesofindia.indiatimes.com//city/madurai/2-accidents-involving-temporary-drivers-reported-in-city/articleshow/62421370.cms",
"http://timesofindia.indiatimes.com//city/ahmedabad/six-year-old-killed-in-lift-accident/articleshow/62420951.cms",
"http://timesofindia.indiatimes.com//city/kochi/2-students-killed-in-truck-accident-near-vazhikkadavu/articleshow/62425811.cms",
"http://timesofindia.indiatimes.com//city/bengaluru/4-accidents-2-deaths-in-13-days-on-sarjapur-road/articleshow/62435372.cms",
"http://timesofindia.indiatimes.com//city/chandigarh/woman-among-2-die-in-accidents-in-zirakpur/articleshow/62435355.cms",
"http://timesofindia.indiatimes.com//city/chandigarh/wrestler-sukhchain-singh-cheema-dies-in-road-accident/articleshow/62455717.cms",
"http://timesofindia.indiatimes.com//city/chennai/four-including-elderly-couple-killed-in-separate-road-accidents/articleshow/62480851.cms",
"http://timesofindia.indiatimes.com//sports/more-sports/wrestling/five-wrestlers-among-six-killed-in-maharashtra-road-accident/articleshow/62484183.cms",
"http://timesofindia.indiatimes.com//city/kolkata/girl-pilgrim-killed-in-accidents/articleshow/62491998.cms",
"http://timesofindia.indiatimes.com//city/kolhapur/5-wrestlers-killed-in-maha-road-accident/articleshow/62492082.cms",
"http://timesofindia.indiatimes.com//city/kolkata/woman-killed-8-others-injured-in-bus-accident/articleshow/62497097.cms",
"http://timesofindia.indiatimes.com//city/mysuru/hassan-accident-a-result-of-human-error-ksrtc/articleshow/62500818.cms",
"http://timesofindia.indiatimes.com//city/jaipur/nine-killed-several-injured-in-two-separate-road-accidents-in-state/articleshow/62501506.cms",
"http://timesofindia.indiatimes.com//city/delhi/3-die-2-injured-in-4-accidents-on-killer-ring-road-section/articleshow/62515034.cms",
"http://timesofindia.indiatimes.com//city/pune/three-killed-in-accident-near-shikrapur/articleshow/62515041.cms",
"http://timesofindia.indiatimes.com//city/coimbatore/3-people-killed-in-separate-road-accidents/articleshow/62515101.cms",
"http://timesofindia.indiatimes.com//city/trichy/four-killed-in-separate-accidents-on-pongal-day/articleshow/62515222.cms",
"http://timesofindia.indiatimes.com//city/rajkot/two-accidents-claim-three-lives/articleshow/62514709.cms",
"http://timesofindia.indiatimes.com//city/rajkot/nine-friends-from-gondal-village-killed-in-accident/articleshow/62514585.cms",
"http://timesofindia.indiatimes.com//city/vadodara/two-groups-clash-over-minor-accident/articleshow/62515130.cms",
"http://timesofindia.indiatimes.com//city/nagpur/doctors-reconstruct-disfigured-face-of-road-accident-victim/articleshow/62531230.cms",
"http://timesofindia.indiatimes.com//city/rajkot/woman-father-in-law-killed-in-accident/articleshow/62530441.cms",
"http://timesofindia.indiatimes.com//city/goa/3-persons-hurt-in-two-accidents-at-bicholim/articleshow/62546533.cms",
"http://timesofindia.indiatimes.com//city/pune/mact-grants-rs-1-39cr-damages-to-kin-of-accident-victim/articleshow/62546424.cms",
"http://timesofindia.indiatimes.com//city/coimbatore/2-college-students-killed-in-road-accidents/articleshow/62561427.cms",
"http://timesofindia.indiatimes.com//city/ludhiana/accident-case-turns-out-murder-7-months-after-crime/articleshow/62575498.cms",
"http://timesofindia.indiatimes.com//city/goa/one-dead-one-injured-in-accident-at-karaswada/articleshow/62596556.cms",
"http://timesofindia.indiatimes.com//city/chennai/four-herbal-farm-workers-die-in-tn-road-accident/articleshow/62602271.cms",
"http://timesofindia.indiatimes.com//city/madurai/seven-killed-in-separate-accidents-near-srivilliputhur/articleshow/62610741.cms",
"http://timesofindia.indiatimes.com//city/noida/loni-mlas-son-injured-in-car-accident/articleshow/62610837.cms",
"http://timesofindia.indiatimes.com//city/patna/two-teenagers-killed-in-accident-near-masaurhi/articleshow/62609440.cms",
"http://timesofindia.indiatimes.com//city/surat/3-from-city-killed-in-accident-in-navsari/articleshow/62609631.cms",
"http://timesofindia.indiatimes.com//city/trichy/two-killed-three-injured-in-separate-road-accidents/articleshow/62626288.cms",
"http://timesofindia.indiatimes.com//city/indore/magisterial-probe/articleshow/62656878.cms",
"http://timesofindia.indiatimes.com//city/goa/maharashtra-native-dies-in-accident-in-sal/articleshow/62641528.cms",
"http://timesofindia.indiatimes.com//city/vadodara/liquor-bag-flung-from-bike-landed-in-car-after-accident/articleshow/62641348.cms",
"http://timesofindia.indiatimes.com//city/hubballi/two-killed-in-accident-on-nh-66/articleshow/62641108.cms",
"http://timesofindia.indiatimes.com//city/salem/solatium-announced-for-victims-of-jan-15-shoolagiri-accident/articleshow/62657157.cms",
"http://timesofindia.indiatimes.com//city/agartala/five-killed-in-tripura-road-accidents/articleshow/62671334.cms",
"http://timesofindia.indiatimes.com//city/kanpur/kanpur-accident-claims-three-lives-deceased-include-a-class-x-student/articleshow/62676973.cms",
"http://timesofindia.indiatimes.com//city/indore/magisterial-report-dpss-bus-accident-caused-due-to-human-error/articleshow/62677068.cms",
"http://timesofindia.indiatimes.com//city/kolhapur/12-of-family-among-13-killed-as-bus-plunges-into-river/articleshow/62678046.cms",
"http://timesofindia.indiatimes.com//city/vadodara/two-godhra-cops-killed-in-road-accident/articleshow/62677268.cms",
"http://timesofindia.indiatimes.com//city/rajkot/two-kids-die-in-different-accidents/articleshow/62686189.cms",
"http://timesofindia.indiatimes.com//city/coimbatore/two-men-killed-in-road-accident/articleshow/62701531.cms",
"http://timesofindia.indiatimes.com//city/chandigarh/rewari-town-planner-dies-in-accident/articleshow/62719412.cms",
"http://timesofindia.indiatimes.com//city/hyderabad/speeding-car-crashes-into-tree-three-techies-die/articleshow/62687381.cms",
"http://timesofindia.indiatimes.com//city/ahmedabad/man-son-die-in-sg-road-crash/articleshow/62676902.cms",
"http://timesofindia.indiatimes.com//city/ghaziabad/3-cisf-men-among-7-injured-as-suv-crashes-into-pole/articleshow/62626682.cms",
"http://timesofindia.indiatimes.com//city/trichy/two-die-in-car-crash-near-manapparai/articleshow/62596710.cms",
"http://timesofindia.indiatimes.com//city/delhi/1-dies-4-hurt-as-suv-crashes-in-shahdara/articleshow/62575393.cms",
"http://timesofindia.indiatimes.com/city/indore/tn-accident-main/articleshow/62561004.cms?",
"http://timesofindia.indiatimes.com/city/ahmedabad/car-crashes-into-house-60-year-old-woman-killed/articleshow/62546542.cms?"
]

    def parse(self, response):
            title = response.xpath('//div[@class="main-content"]/section/h1/arttitle/text()').extract_first()
            # title = response.xpath('//td[@align="left"]/span/a/text()').extract()
            # location = response.xpath('//div[@id="artLocation"]/div/text()').extract_first()
            # source = response.xpath('//div[@id="artSource"]/div/text()').extract_first()
            # top_line = response.xpath('//div[@id="divArticleContent"]/text()').extract_first()
            # lines = response.xpath('//div[@id="divArticleContent"]/p/text()').extract()
        
            yield {
            'title' : title
            }

            # yield {
            # 'title' : title,
            # 'location' : location,
            # 'source' : source,
            # 'top-line':  top_line,
            # 'lines':  lines,
        # }

    # def parse(self, response):
    #         yield {
    #         'title' : response.xpath('//div[@id="divTitle"]/text()').extract_first(),
    #         'location' : response.xpath('//div[@id="artLocation"]/div/text()').extract_first(),
    #         'source' : response.xpath('//div[@id="artSource"]/div/text()').extract_first(),
    #         'top-line':  response.xpath('//div[@id="divArticleContent"]/text()').extract_first(),
    #         'lines':  response.xpath('//div[@id="divArticleContent"]/p/text()').extract(),
    #     }