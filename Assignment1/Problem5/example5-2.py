import json

tweet = r'''{"created_at":"Sun Jul 06 13:37:00 +0000 2014","id":485779449057910784,"id_str":"485779449057910784","text":"RT @RealPromoKing: [NewMusic] @RealYoungBanks - ''Foreign Whip'' https:\/\/t.co\/LApXKZY7Au (Hosted By @OfficialKushGod) #1017MafiaGang","source":"\u003ca href=\"http:\/\/twitter.com\/download\/android\" rel=\"nofollow\"\u003eTwitter for Android\u003c\/a\u003e","truncated":false,"in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":null,"in_reply_to_user_id_str":null,"in_reply_to_screen_name":null,"user":{"id":308917839,"id_str":"308917839","name":"Young Banks [1017MG]","screen_name":"RealYoungBanks","location":"Montreal [RealCity] , Canada","url":"http:\/\/youngbanks.com","description":"1017 Mafia Gang Recording Artist - https:\/\/itunes.apple.com\/ca\/album\/manute-bol-money-single\/id826055954 (Booking:438-807-4858) #1017MafiaGang #FreeGuwop","protected":false,"followers_count":35811,"friends_count":293,"listed_count":9,"created_at":"Wed Jun 01 06:39:52 +0000 2011","favourites_count":225,"utc_offset":-14400,"time_zone":"Eastern Time (US & Canada)","geo_enabled":false,"verified":false,"statuses_count":5788,"lang":"en","contributors_enabled":false,"is_translator":false,"is_translation_enabled":false,"profile_background_color":"131516","profile_background_image_url":"http:\/\/abs.twimg.com\/images\/themes\/theme14\/bg.gif","profile_background_image_url_https":"https:\/\/abs.twimg.com\/images\/themes\/theme14\/bg.gif","profile_background_tile":true,"profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/476907525833768960\/0mhALYcs_normal.jpeg","profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/476907525833768960\/0mhALYcs_normal.jpeg","profile_banner_url":"https:\/\/pbs.twimg.com\/profile_banners\/308917839\/1402692558","profile_link_color":"610000","profile_sidebar_border_color":"EEEEEE","profile_sidebar_fill_color":"EFEFEF","profile_text_color":"333333","profile_use_background_image":true,"default_profile":false,"default_profile_image":false,"following":null,"follow_request_sent":null,"notifications":null},"geo":null,"coordinates":null,"place":null,"contributors":null,"retweeted_status":{"created_at":"Sun Jul 06 10:00:08 +0000 2014","id":485724870223736832,"id_str":"485724870223736832","text":"[NewMusic] @RealYoungBanks - ''Foreign Whip'' https:\/\/t.co\/LApXKZY7Au (Hosted By @OfficialKushGod) #1017MafiaGang","source":"\u003ca href=\"http:\/\/twuffer.com\" rel=\"nofollow\"\u003eTwuffer\u003c\/a\u003e","truncated":false,"in_reply_to_status_id":null,"in_reply_to_status_id_str":null,"in_reply_to_user_id":null,"in_reply_to_user_id_str":null,"in_reply_to_screen_name":null,"user":{"id":2190366897,"id_str":"2190366897","name":"PromoKing \/ KingA","screen_name":"RealPromoKing","location":"","url":"http:\/\/kingapromo.dx.am","description":"Follow @kingApromo @RealYoungBanks [Email::kingapromotion@gmail.com]","protected":false,"followers_count":438,"friends_count":99,"listed_count":0,"created_at":"Thu Nov 21 20:10:19 +0000 2013","favourites_count":16,"utc_offset":null,"time_zone":null,"geo_enabled":false,"verified":false,"statuses_count":3960,"lang":"en","contributors_enabled":false,"is_translator":false,"is_translation_enabled":false,"profile_background_color":"C0DEED","profile_background_image_url":"http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png","profile_background_image_url_https":"https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png","profile_background_tile":false,"profile_image_url":"http:\/\/pbs.twimg.com\/profile_images\/453298345860423680\/hBMHXhQr_normal.jpeg","profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/453298345860423680\/hBMHXhQr_normal.jpeg","profile_banner_url":"https:\/\/pbs.twimg.com\/profile_banners\/2190366897\/1396909710","profile_link_color":"0084B4","profile_sidebar_border_color":"C0DEED","profile_sidebar_fill_color":"DDEEF6","profile_text_color":"333333","profile_use_background_image":true,"default_profile":true,"default_profile_image":false,"following":null,"follow_request_sent":null,"notifications":null},"geo":null,"coordinates":null,"place":null,"contributors":null,"retweet_count":4,"favorite_count":0,"entities":{"hashtags":[{"text":"1017MafiaGang","indices":[99,113]}],"symbols":[],"urls":[{"url":"https:\/\/t.co\/LApXKZY7Au","expanded_url":"https:\/\/www.youtube.com\/watch?v=31CEGe3ygGk","display_url":"youtube.com\/watch?v=31CEGe\u2026","indices":[46,69]}],"user_mentions":[{"screen_name":"RealYoungBanks","name":"Young Banks [1017MG]","id":308917839,"id_str":"308917839","indices":[11,26]},{"screen_name":"OfficialKushGod","name":"DJ KKG\u00ae\/Darth Ku$h","id":231161062,"id_str":"231161062","indices":[81,97]}]},"favorited":false,"retweeted":false,"possibly_sensitive":false,"lang":"en"},"retweet_count":0,"favorite_count":0,"entities":{"hashtags":[{"text":"1017MafiaGang","indices":[118,132]}],"symbols":[],"urls":[{"url":"https:\/\/t.co\/LApXKZY7Au","expanded_url":"https:\/\/www.youtube.com\/watch?v=31CEGe3ygGk","display_url":"youtube.com\/watch?v=31CEGe\u2026","indices":[65,88]}],"user_mentions":[{"screen_name":"RealPromoKing","name":"PromoKing \/ KingA","id":2190366897,"id_str":"2190366897","indices":[3,17]},{"screen_name":"RealYoungBanks","name":"Young Banks [1017MG]","id":308917839,"id_str":"308917839","indices":[30,45]},{"screen_name":"OfficialKushGod","name":"DJ KKG\u00ae\/Darth Ku$h","id":231161062,"id_str":"231161062","indices":[100,116]}]},"favorited":false,"retweeted":false,"possibly_sensitive":false,"filter_level":"medium","lang":"en"}'''
message = json.loads(tweet)
location = message['user']['location']
print location
