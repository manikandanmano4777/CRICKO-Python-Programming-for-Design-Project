import discord
from discord.ext import commands
from discord.ui import Button, View, Select
import asyncio
import random
import select


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="cc ", intents=intents)

ipl_teams = {
    "MI": {"name": "Mumbai Indians", "purse": 45_00_00_000, "retained_players": ["Rohit Sharma", "Suryakumar Yadav", "Jasprit Bumrah", "Tilak Varma", "Hardik Pandya"], "rtm": 0},
    "CSK": {"name": "Chennai Super Kings", "purse": 55_00_00_000, "retained_players": ["MS Dhoni", "Ravindra Jadeja", "Ruturaj Gaikwad", "Shivam Dube", "Matheesha Pathirana"], "rtm": 0},
    "RCB": {"name": "Royal Challengers Bangalore", "purse": 83_00_00_000, "retained_players": ["Virat Kohli", "Rajat Patidar", "Yash Dayal"], "rtm": 0},
    "DC": {"name": "Delhi Capitals", "purse": 73_00_00_000, "retained_players": ["Axar Patel", "Abhishek Porel", "Tristan Stubbs", "Kuldeep Yadav"], "rtm": 0},
    "KKR": {"name": "Kolkata Knight Riders", "purse": 51_00_00_000, "retained_players": ["Sunil Narine", "Rinku Singh", "Andre Russell", "Varun Chakaravarthy", "Harshit Rana", "Ramandeep Singh"], "rtm": 0},
    "SRH": {"name": "Sunrisers Hyderabad", "purse": 45_00_00_000, "retained_players": ["Heinrich Klaasen", "Pat Cummins", "Travis Head", "Abhishek Sharma", "Nitish Kumar Reddy"], "rtm": 0},
    "RR": {"name": "Rajasthan Royals", "purse": 41_00_00_000, "retained_players": ["Sanju Samson", "Riyan Parag", "Yashasvi Jaiswal", "Sandeep Sharma", "Dhruv Jurel", "Shimron Hetmyer"], "rtm": 0},
    "LSG": {"name": "Lucknow Super Giants", "purse": 69_00_00_000, "retained_players": ["Nicholas Pooran", "Mayank Yadav", "Ravi Bishnoi", "Mohsin Khan", "Ayush Badoni"], "rtm": 0},
    "GT": {"name": "Gujarat Titans", "purse": 69_00_00_000, "retained_players": ["Rashid Khan", "Shubman Gill", "Sai Sudharsan", "Rahul Tewatia", "Shahrukh Khan"], "rtm": 0},
    "PBKS": {"name": "Punjab Kings", "purse": 110_50_00_000, "retained_players": ["Shashank Singh", "Prabhsimran Singh"], "rtm": 0}
}


# Player data organized by sets




player_sets = {

"Set 1 M1 - Marquee 1": [
        {"name": "Jos Buttler", "base_price": "Rs 2 crore", "previous_team": "RR", "image": "https://www.teamwass.com/wp-content/uploads/2024/03/Jos-Butler-updated.jpg"},
  {"name": "Shreyas Iyer", "base_price": "Rs 2 crore", "previous_team": "KKR", "image": "https://images.news18.com/ibnlive/uploads/2024/03/shreyas-iyer-india-bcci-2024-03-346d0bf0c2a6495af0c809a61f2648e6-3x2.jpg"},
  {"name": "Rishabh Pant", "base_price": "Rs 2 crore", "previous_team": "DC", "image": "https://c.ndtvimg.com/2024-08/v2kdqi38_rishabh-pant-afp_625x300_16_August_24.jpg?im=FeatureCrop,algorithm=dnn,width=806,height=605"},
  {"name": "Kagiso Rabada", "base_price": "Rs 2 crore", "previous_team": "PBKS", "image": "https://assets.khelnow.com/news/uploads/2024/10/Kagiso-Rabada-test-cricket.jpg"},
  {"name": "Arshdeep Singh", "base_price": "Rs 2 crore", "previous_team": "PBKS", "image": "https://static.cricketaddictor.com/images/ArshdeepSingh.webp?q=80"},
  {"name": "Mitchell Starc", "base_price": "Rs 2 crore", "previous_team": "KKR", "image": "https://cdn.siasat.com/wp-content/uploads/2023/12/Untitled-design-2023-12-19T190822.642.jpg"},
    ],

    
"Set 2 M2 - Marquee 2": [ 
    {"name": "Yuzvendra Chahal", "base_price": "Rs 2 crore", "previous_team": "RR", "image": "https://c.ndtvimg.com/2023-08/aup1ebbo_yuzvendra-chahal-afp_625x300_06_August_23.jpg?im=FeatureCrop,algorithm=dnn,width=806,height=605g"},
  {"name": "Liam Livingstone", "base_price": "Rs 2 crore", "previous_team": "PBKS", "image": "https://api.bdcrictime.com/liam-livingstone-28_03_2022.jpg"},
  {"name": "David Miller", "base_price": "Rs 1.5 crore", "previous_team": "GT", "image": "https://media.sportstiger.com/media/david-miller-1719992867502-original.webp"},
  {"name": "KL Rahul", "base_price": "Rs 2 crore", "previous_team": "LSG", "image": "https://www.livemint.com/lm-img/img/2024/11/08/1600x900/KL_rahul_1731065636909_1731065637186.jpg"},
  {"name": "Mohammad Shami", "base_price": "Rs 2 crore", "previous_team": "GT", "image": "https://images.news9live.com/wp-content/uploads/2024/11/Mohammed-Shami-Test-1.png?q=50&w=1200"},
  {"name": "Mohammad Siraj", "base_price": "Rs 2 crore", "previous_team": "RCB", "image": "https://images.assettype.com/nationalherald/2023-09/777e091d-3fbe-405b-87d4-2470a280c59f/siraj_v1__1_.jpg"}],





"Set 3 BAT1 - Batsmen 1": [ {"name": "Harry Brook", "base_price": "Rs 2 crore", "previous_team": "DC", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTPtq6kz0tsNQOv4v7yKVTNFfJI9rHEFoM7iA&s"},
    {"name": "Devon Conway", "base_price": "Rs 2 crore", "previous_team": "CSK", "image": "https://static.toiimg.com/thumb/msid-97299295,width-1280,height-720,resizemode-4/97299295.jpg"},
    {"name": "Jake Fraser-Mcgurk", "base_price": "Rs 2 crore", "previous_team": "DC", "image": "https://example.com/jake_fraser_mcgurk.png"},
    {"name": "Aiden Markram", "base_price": "Rs 2 crore", "previous_team": "SRH", "image": "https://images.indianexpress.com/2023/10/South-Africa-Aiden-Markram-PTI-CROP.png"},
    {"name": "Devdutt Padikkal", "base_price": "Rs 2 crore", "previous_team": "LSG", "image": "https://example.com/devdutt_padikkal.png"},
    {"name": "Rahul Tripathi", "base_price": "Rs 75 lakh", "previous_team": "SRH", "image": "https://example.com/rahul_tripathi.png"} ],





"Set 4 FP1 - All Rounders 1": [
  {"name": "Ravichandran Ashwin", "base_price": "Rs 2 crore", "previous_team": "RR", "image": "https://i.ytimg.com/vi/G1p6euDdAHU/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLAHWmueJ9oqmfFkrp7aDZ4ZiTewvA"},
  {"name": "Venkatesh Iyer", "base_price": "Rs 2 crore", "previous_team": "KKR", "image": "https://i.ytimg.com/vi/G1p6euDdAHU/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLAHWmueJ9oqmfFkrp7aDZ4ZiTewvA"},
  {"name": "Mitchell Marsh", "base_price": "Rs 2 crore", "previous_team": "DC", "image": "https://i.ytimg.com/vi/G1p6euDdAHU/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLAHWmueJ9oqmfFkrp7aDZ4ZiTewvA"},
  {"name": "Glenn Maxwell", "base_price": "Rs 2 crore", "previous_team": "RCB", "image": "https://i.ytimg.com/vi/G1p6euDdAHU/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLAHWmueJ9oqmfFkrp7aDZ4ZiTewvAg"},
  {"name": "Harshal Patel", "base_price": "Rs 2 crore", "previous_team": "PBKS", "image": "https://i.ytimg.com/vi/G1p6euDdAHU/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLAHWmueJ9oqmfFkrp7aDZ4ZiTewvA"},
  {"name": "Rachin Ravindra", "base_price": "Rs 1.5 crore", "previous_team": "CSK", "image": "https://i.ytimg.com/vi/G1p6euDdAHU/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLAHWmueJ9oqmfFkrp7aDZ4ZiTewvA"},
    {"name": "Marcus Stoinis", "base_price": "Rs 2 crore", "previous_team": "LSG", "image": "https://i.ytimg.com/vi/G1p6euDdAHU/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLAHWmueJ9oqmfFkrp7aDZ4ZiTewvAg"},
],




"Set 5 WK1 - Wicket-keepers 1": [
  {"name": "Jonny Bairstow", "base_price": "Rs 2 crore", "previous_team": "PBKS", "image": "https://example.com/jonny_bairstow_image"},
  {"name": "Quinton de Kock", "base_price": "Rs 2 crore", "previous_team": "LSG", "image": "https://akm-img-a-in.tosshub.com/indiatoday/images/story/202312/quinton-de-kock-014342686-1x1.jpg?VersionId=gIWyLgSW.QHJzU_rR1Qn9Ml9u7g7r5GG"},
  {"name": "Rahmanullah Gurbaz", "base_price": "Rs 2 crore", "previous_team": "KKR", "image": "https://example.com/rahmanullah_gurbaz_image"},
  {"name": "Ishan Kishan", "base_price": "Rs 2 crore", "previous_team": "MI", "image": "https://library.sportingnews.com/styles/twitter_card_120x120/s3/2023-10/Ishan%20Kishan%20India.jpg?itok=mZgeCyEg"},
  {"name": "Phil Salt", "base_price": "Rs 2 crore", "previous_team": "KKR", "image": "https://example.com/phil_salt_image"},
  {"name": "Jitesh Sharma", "base_price": "Rs 2 crore", "previous_team": "PBKS", "image": "https://example.com/jitesh_sharma_image"}
],


"Set 6 FP1 - Fast Bowlers 1": [
    {"name": "Syed Khaleel Ahmed", "base_price": "Rs 2 crore", "previous_team": "DC", "image": "https://example.com/syed_khaleel_ahmed_image"},
    {"name": "Trent Boult", "base_price": "Rs 2 crore", "previous_team": "RR", "image": "https://api.bdcrictime.com/trent-boult-07_04_2022.jpg"},
    {"name": "Josh Hazlewood", "base_price": "Rs 2 crore", "previous_team": "Unspecified", "image": "https://upload.wikimedia.org/wikipedia/commons/7/77/2018.01.21.17.06.41-Hazelwood_%2839139885264%29.jpg"},
    {"name": "Avesh Khan", "base_price": "Rs 2 crore", "previous_team": "RR", "image": "https://example.com/avesh_khan_image"},
    {"name": "Prasidh Krishna", "base_price": "Rs 2 crore", "previous_team": "RR", "image": "https://example.com/prasidh_krishna_image"},
    {"name": "T. Natarajan", "base_price": "Rs 2 crore", "previous_team": "SRH", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSYf1tHsoF6OmzJAJpdbGKgfeJr2FtLaUWBaA&s"},
    {"name": "Anrich Nortje", "base_price": "Rs 2 crore", "previous_team": "DC", "image": "https://example.com/anrich_nortje_image"},
  ],

"Set 7: SP1 - Spin Bowlers": [
    {"name": "Noor Ahmad", "base_price": "Rs 2 crore", "previous_team": "GT", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSF8ouUZ9wJUg_D7jp1Rzd8cKSOqvOcmmSMAw&se"},
    {"name": "Rahul Chahar", "base_price": "Rs 2 crore", "previous_team": "PBKS", "image": "https://example.com/rahul_chahar_image"},
    {"name": "Wanindu Hasaranga", "base_price":"Rs 2 crore", "previous_team": "SRH", "image": "https://example.com/wanindu_hasaranga_image"},
    {"name": "Waqar Salamkheil", "base_price": "Rs 2 crore", "previous_team": "Unspecified", "image": "https://example.com/waqar_salamkheil_image"},
    {"name": "Maheesh Theekshana", "base_price": "Rs 2 crore", "previous_team": "CSK", "image": "https://images.indianexpress.com/2024/07/Maheesh-Theekshana.jpg"},
    {"name": "Adam Zampa", "base_price": "Rs 2 crore", "previous_team": "RR", "image": "https://www.hindustantimes.com/ht-img/img/2024/04/11/1600x900/CRICKET-NZL-AUS-10_1712840279058_1712840320689.jpg"}
  ],



"Set 8: UBA1 - Uncapped Batters": [
    {"name": "Yash Dhull", "base_price": "Rs 30 lakh", "previous_team": "DC", "image": "https://images-cricketcom.imgix.net/news-1731650012601"},
    {"name": "Abhinav Manohar", "base_price": "Rs 30 lakh", "previous_team": "GT", "image": "https://images-cricketcom.imgix.net/news-1731650012601"},
    {"name": "Karun Nair", "base_price": "Rs 30 lakh", "previous_team": "Unspecified", "image": "https://images-cricketcom.imgix.net/news-1731650012601"},
    {"name": "Angkrish Raghuvanshi", "base_price": "Rs 30 lakh", "previous_team": "KKR", "image": "https://images-cricketcom.imgix.net/news-1731650012601"},
    {"name": "Anmolpreet Singh", "base_price": "Rs 30 lakh", "previous_team": "SRH", "image": "https://images-cricketcom.imgix.net/news-1731650012601"},
    {"name": "Atharva Taide", "base_price": "Rs 30 lakh", "previous_team": "PBKS", "image": "https://images-cricketcom.imgix.net/news-1731650012601"},
    {"name": "Nehal Wadhera", "base_price": "Rs 30 lakh", "previous_team": "MI", "image": "https://images-cricketcom.imgix.net/news-1731650012601"}
],

"Set 9: UAL1 - Uncapped All-rounders": [
    {"name": "Harpreet Brar", "base_price": "Rs 30 lakh", "previous_team": "PBKS", "image": "https://example.com/harpreet_brar_image"},
    {"name": "Naman Dhir", "base_price": "Rs 30 lakh", "previous_team": "MI", "image": "https://example.com/naman_dhir_image"},
    {"name": "Mahipal Lomror", "base_price": "Rs 50 lakh", "previous_team": "RCB", "image": "https://example.com/mahipal_lomror_image"},
    {"name": "Sameer Rizvi", "base_price": "Rs 30 lakh", "previous_team": "CSK", "image": "https://example.com/sameer_rizvi_image"},
    {"name": "Abdul Samad", "base_price": "Rs 30 lakh", "previous_team": "SRH", "image": "https://example.com/abdul_samad_image"},
    {"name": "Vijay Shankar", "base_price": "Rs 30 lakh", "previous_team": "GT", "image": "https://example.com/vijay_shankar_image"},
    {"name": "Ashutosh Sharma", "base_price": "Rs 30 lakh", "previous_team": "PBKS", "image": "https://example.com/ashutosh_sharma_image"},
    {"name": "Nishant Sindhu", "base_price": "Rs 30 lakh", "previous_team": "CSK", "image": "https://example.com/nishant_sindhu_image"},
    {"name": "Utkarsh Singh", "base_price": "Rs 30 lakh", "previous_team": "PBKS", "image": "https://example.com/utkarsh_singh_image"}
],

"Set 10: UWK1 - Uncapped Wicketkeepers": [
    {"name": "Aryan Juyal", "base_price": "Rs 30 lakh", "previous_team": "MI", "image": "https://example.com/aryan_juyal_image"},
    {"name": "Kumar Kushagra", "base_price": "Rs 30 lakh", "previous_team": "GT", "image": "https://example.com/kumar_kushagra_image"},
    {"name": "Robin Minz", "base_price": "Rs 30 lakh", "previous_team": "GT", "image": "https://example.com/robin_minz_image"},
    {"name": "Anuj Rawat", "base_price": "Rs 30 lakh", "previous_team": "RCB", "image": "https://example.com/anuj_rawat_image"},
    {"name": "Luvnith Sisodia", "base_price": "Rs 30 lakh", "previous_team": "RCB", "image": "https://example.com/luv_nith_sisodia_image"},
    {"name": "Vishnu Vinod", "base_price": "Rs 30 lakh", "previous_team": "MI", "image": "https://example.com/vishnu_vinod_image"},
    {"name": "Upendra Singh Yadav", "base_price": "Rs 30 lakh", "previous_team": "SRH", "image": "https://example.com/upendra_singh_yadav_image"}
],

"Set 11: UFA1 - Fast Bowlers": [
    {"name": "Vaibhav Arora", "base_price": "Rs 30 lakh", "previous_team": "KKR", "image": "https://example.com/vaibhav_arora_image"},
    {"name": "Rasikh Dar", "base_price": "Rs 30 lakh", "previous_team": "DC", "image": "https://example.com/rasikh_dar_image"},
    {"name": "Akash Madhwal", "base_price": "Rs 30 lakh", "previous_team": "MI", "image": "https://example.com/akash_madhwal_image"},
    {"name": "Mohit Sharma", "base_price": "Rs 50 lakh", "previous_team": "GT", "image": "https://cf-images.eu-west-1.prod.boltdns.net/v1/static/3588749423001/f07ad8e3-dae1-4ead-a5c7-406e03168d1c/be8b9ffe-1265-4921-84a2-6792f91ae6fe/1280x720/match/image.jpg"},
    {"name": "Simarjeet Singh", "base_price": "Rs 30 lakh", "previous_team": "CSK", "image": "https://images-cricketcom.imgix.net/news-1715518611282?auto=compress,format&dpr=1&w=976&h400&q=80"},
    {"name": "Yash Thakur", "base_price": "Rs 30 lakh", "previous_team": "LSG", "image": "https://example.com/yash_thakur_image"},
    {"name": "Kartik Tyagi", "base_price": "Rs 40 lakh", "previous_team": "GT", "image": "https://example.com/kartik_tyagi_image"},
    {"name": "Vyshak Vijaykumar", "base_price": "Rs 30 lakh", "previous_team": "RCB", "image": "https://example.com/vyshak_vijaykumar_image"}
],

"Set 12: USP1 - Uncapped Spinners": [
    {"name": "Piyush Chawla", "base_price": "Rs 50 lakh", "previous_team": "MI", "image": "https://example.com/piyush_chawla_image"},
    {"name": "Shreyas Gopal", "base_price": "Rs 30 lakh", "previous_team": "RR", "image": "https://example.com/shreyas_gopal_image"},
    {"name": "Mayank Markande", "base_price": "Rs 30 lakh", "previous_team": "MI", "image": "https://example.com/mayank_markande_image"},
    {"name": "Suyash Sharma", "base_price": "Rs 30 lakh", "previous_team": "KKR", "image": "https://example.com/suyash_sharma_image"},
    {"name": "Karn Sharma", "base_price": "Rs 50 lakh", "previous_team": "CSK", "image": "https://example.com/karn_sharma_image"},
    {"name": "Kumar Kartikeya Singh", "base_price": "Rs 30 lakh", "previous_team": "MI", "image": "https://example.com/kumar_kartikeya_singh_image"},
    {"name": "Manav Suthar", "base_price": "Rs 30 lakh", "previous_team": "GT", "image": "https://example.com/manav_suthar_image"}
],



"Set 13: BA2 - Capped Batsmen": [
    {"name": "Mayank Agarwal", "base_price": "Rs 1 crore", "previous_team": "PBKS", "image": "https://example.com/mayank_agarwal_image"},
    {"name": "Faf Du Plessis", "base_price": "Rs 2 crore", "previous_team": "RCB", "image": "https://crictoday.com/wp-content/uploads/2023/03/Faf-du-Plessis-crictoday.jpg"},
    {"name": "Glenn Phillips", "base_price": "Rs 2 crore", "previous_team": "RR", "image": "https://example.com/glenn_phillips_image"},
    {"name": "Rovman Powell", "base_price": "Rs 1.5 crore", "previous_team": "RR", "image": "https://example.com/rovman_powell_image"},
    {"name": "Ajinkya Rahane", "base_price": "Rs 1.5 crore", "previous_team": "MI", "image": "https://example.com/ajinkya_rahane_image"},
    {"name": "Prithvi Shaw", "base_price": "Rs 75 lakh", "previous_team": "DC", "image": "https://example.com/prithvi_shaw_image"},
    {"name": "Kane Williamson", "base_price": "Rs 2 crore", "previous_team": "GT", "image": "https://crictoday.com/wp-content/uploads/2023/03/Williamson_1200x768.webp"}
],




    "Set 14: AL2 - Capped All-Rounders": [
    {"name": "Sam Curran", "base_price": "Rs 2 crore", "previous_team": "CSK", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_dgpIk5-61eRZfQi5j1vGPnHSyTrEHdmLZw&s"},
    {"name": "Marco Jansen", "base_price": "Rs 1.25 crore", "previous_team": "SRH", "image": "https://upload.wikimedia.org/wikipedia/commons/4/41/Marco_Jansen_2022.jpg"},
    {"name": "Daryl Mitchell", "base_price": "Rs 2 crore", "previous_team": "CSK", "image": "https://akm-img-a-in.tosshub.com/indiatoday/images/story/202310/new-zealands-daryl-mitchell-224945569-3x4.jpg?VersionId=k8GzsV45eZ_ALHwQ2raeKbOr5HM8fpN2e"},
    {"name": "Krunal Pandya", "base_price": "Rs 2 crore", "previous_team": "LSG", "image": "https://example.com/krunal_pandya_image"},
    {"name": "Nitish Rana", "base_price": "Rs 1.5 crore", "previous_team": "KKR", "image": "https://example.com/nitish_rana_image"},
    {"name": "Washington Sundar", "base_price": "Rs 2 crore", "previous_team": "SRH", "image": "https://crictoday.com/wp-content/uploads/2023/02/washington-sundar.jpg"},
    {"name": "Shardul Thakur", "base_price": "Rs 2 crore", "previous_team": "CSK", "image": "https://example.com/shardul_thakur_image"}
  ],
  "Set 15: WK2 - Capped Wicketkeepers": [
    {"name": "K.S Bharat", "base_price": "Rs 75 lakh", "previous_team": "KKR", "image": "https://example.com/ks_bharat_image"},
    {"name": "Alex Carey", "base_price": "Rs 1 crore", "previous_team": "DC", "image": "https://example.com/alex_carey_image"},
    {"name": "Donovan Ferreira", "base_price": "Rs 75 lakh", "previous_team": "RR", "image": "https://example.com/donovan_ferreira_image"},
    {"name": "Shai Hope", "base_price": "Rs 1.25 crore", "previous_team": "DC", "image": "https://example.com/shai_hope_image"},
    {"name": "Josh Inglis", "base_price": "Rs 2 crore", "previous_team": "DC", "image": "https://example.com/josh_inglis_image"},
    {"name": "Ryan Rickelton", "base_price": "Rs 1 crore", "previous_team": "DC", "image": "https://example.com/ryan_rickelton_image"}
  ],
  "Set 16: FA2 - Capped Fast Bowlers": [
    {"name": "Deepak Chahar", "base_price": "Rs 2 crore", "previous_team": "CSK", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTRKmDBzsAMLlEhPRzXXhRVLNZrIPLFbJRFDQ&s"},
    {"name": "Gerald Coetzee", "base_price": "Rs 1.25 crore", "previous_team": "MI", "image": "https://example.com/gerald_coetzee_image"},
    {"name": "Akash Deep", "base_price": "Rs 1 crore", "previous_team": "RCB", "image": "https://example.com/akash_deep_image"},
    {"name": "Tushar Deshpande", "base_price": "Rs 1 crore", "previous_team": "DC, CSK", "image": "https://example.com/tushar_deshpande_image"},
    {"name": "Lockie Ferguson", "base_price": "Rs 2 crore", "previous_team": "RCB", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8Gjfanpr5BwZJSYzCDIYLxwSx8gBrS9wNTw&s"},
    {"name": "Bhuvneshwar Kumar", "base_price": "Rs 2 crore", "previous_team": "SRH", "image": "https://s3.ap-south-1.amazonaws.com/image.cricket.com/articles/b0f15e2ad6b796912827475767ced77d3b212321.png"},
    {"name": "Mukesh Kumar", "base_price": "Rs 2 crore", "previous_team": "DC", "image": "https://example.com/mukesh_kumar_image"}
  ],
  "Set 17: SP2 - Capped Spinners": [
    {"name": "Allah Ghazanfar", "base_price": "Rs 75 lakh", "previous_team": "KKR", "image": "https://example.com/allah_ghazanfar_image"},
    {"name": "Akeal Hosein", "base_price": "Rs 1.5 crore", "previous_team": "SRH", "image": "https://example.com/akeal_hosein_image"},
    {"name": "Keshav Maharaj", "base_price": "Rs 75 lakh", "previous_team": "RR", "image": "https://example.com/keshav_maharaj_image"},
    {"name": "Mujeeb Ur Rahman", "base_price": "Rs 2 crore", "previous_team": "PBKS", "image": "https://example.com/mujeeb_ur_rahman_image"},
    {"name": "Adil Rashid", "base_price": "Rs 2 crore", "previous_team": "PBKS, SRH", "image": "https://example.com/adil_rashid_image"},
    {"name": "Vijayakanth Viyaskanth", "base_price": "Rs 75 lakh", "previous_team": "SRH", "image": "https://example.com/vijayakanth_viyaskanth_image"}
  ],
  "Set 18: UBA2 - Uncapped Batsmen": [
    {"name": "Swastik Chhikara", "base_price": "Rs 30 lakh", "previous_team": "DC", "image": "https://example.com/swastik_chhikara_image"},
    {"name": "Aarya Desai", "base_price": "Rs 30 lakh", "previous_team": "KKR", "image": "https://example.com/aarya_desai_image"},
    {"name": "Shubham Dubey", "base_price": "Rs 30 lakh", "previous_team": "RR", "image": "https://example.com/shubham_dubey_image"},
    {"name": "Shaik Rasheed", "base_price": "Rs 30 lakh", "previous_team": "CSK", "image": "https://example.com/shaik_rasheed_image"},
    {"name": "Himmat Singh", "base_price": "Rs 30 lakh", "previous_team": "RCB", "image": "https://example.com/himmat_singh_image"}
  ],
  "Set 19: UAL2 - Uncapped All-Rounders": [
    {"name": "Mayank Dagar", "base_price": "Rs 30 lakh", "previous_team": "PBKS", "image": "https://example.com/mayank_dagar_image"},
    {"name": "Anshul Kamboj", "base_price": "Rs 30 lakh", "previous_team": "MI", "image": "https://example.com/anshul_kamboj_image"},
    {"name": "Mohd. Arshad Khan", "base_price": "Rs 30 lakh", "previous_team": "RCB", "image": "https://example.com/mohd_arshad_khan_image"},
    {"name": "Nishant Pandey", "base_price": "Rs 30 lakh", "previous_team": "DC", "image": "https://example.com/nishant_pandey_image"},
    {"name": "Rehan Ahmed", "base_price": "Rs 30 lakh", "previous_team": "None", "image": "https://example.com/rehan_ahmed_image"},
    {"name": "Gurnoor Singh", "base_price": "Rs 30 lakh", "previous_team": "None", "image": "https://example.com/gurnoor_singh_image"}
  ],


"Set 20: UFA2 - Uncapped Players": [
    {"name": "Gurnoor Singh Brar", "base_price": "Rs 30 lakh", "previous_team": "PBKS","image": "https://example.com/gurnoor_singh_brar_image"},
    {"name": "Mukesh Choudhary", "base_price": "Rs 30 lakh", "previous_team": "CSK", "image": "https://example.com/mukesh_choudhary_image"},
    {"name": "Sakib Hussain", "base_price": "Rs 30 lakh", "previous_team": "KKR", "image": "https://example.com/sakib_hussain_image"},
    {"name": "Vidwath Kaverappa", "base_price": "Rs 30 lakh", "previous_team": "PBKS", "image": "https://example.com/vidwath_kaverappa_image"},
    {"name": "Rajan Kumar", "base_price": "Rs 30 lakh", "previous_team": "RCB", "image": "https://example.com/rajan_kumar_image"},
    {"name": "Sushant Mishra", "base_price": "Rs 30 lakh", "previous_team": "GT", "image": "https://example.com/sushant_mishra_image"},
    {"name": "Arjun Tendulkar", "base_price": "Rs 30 lakh", "previous_team": "MI", "image": "https://example.com/arjun_tendulkar_image"},
    {"name": "Zeeshan Ansari", "base_price": "Rs 30 lakh", "previous_team": "UPCA", "image": "https://example.com/zeeshan_ansari_image"},
    {"name": "Prince Choudhary", "base_price": "Rs 30 lakh", "previous_team": "DDCA", "image": "https://example.com/prince_choudhary_image"},
    {"name": "Himanshu Sharma", "base_price": "Rs 30 lakh", "previous_team": "RCA", "image": "https://example.com/himanshu_sharma_image"},
    {"name": "M. Siddharth", "base_price": "Rs 30 lakh", "previous_team": "TNCA", "image": "https://example.com/m_siddharth_image"},
    {"name": "Digvesh Singh", "base_price": "Rs 30 lakh", "previous_team": "DDCA", "image": "https://example.com/digvesh_singh_image"},
    {"name": "Prashant Solanki", "base_price": "Rs 30 lakh", "previous_team": "MACA", "image": "https://example.com/prashant_solanki_image"},
    {"name": "Jhathavedh Subramanyan", "base_price": "Rs 30 lakh", "previous_team": "TNCA", "image": "https://example.com/jhathavedh_subramanyan_image"}
],

"Set 21: BA3 - Batsmen": [
    {"name": "Finn Allen", "base_price": "Rs 2 crore", "previous_team": "RCB", "image": "https://example.com/finn_allen_image"},
    {"name": "Dewald Brevis", "base_price": "Rs 75 lakh", "previous_team": "MI", "image": "https://example.com/dewald_brevis_image"},
    {"name": "Ben Duckett", "base_price": "Rs 2 crore", "previous_team": "Capped", "image": "https://example.com/ben_duckett_image"},
    {"name": "Manish Pandey", "base_price": "Rs 75 lakh", "previous_team": "KKR", "image": "https://example.com/manish_pandey_image"},
    {"name": "Rilee Rossouw", "base_price": "Rs 2 crore", "previous_team": "PBKS", "image": "https://example.com/rilee_rossouw_image"},
    {"name": "Sherfane Rutherford", "base_price": "Rs 1.5 crore", "previous_team": "KKR", "image": "https://example.com/sherfane_rutherford_image"},
    {"name": "Ashton Turner", "base_price": "Rs 1 crore", "previous_team": "LSG", "image": "https://example.com/ashton_turner_image"},
    {"name": "James Vince", "base_price": "Rs 2 crore", "previous_team": "Capped", "image": "https://example.com/james_vince_image"}
],

"Set 22: AL3: All-Rounders": [
    {"name": "Shahbaz Ahamad", "base_price": "Rs 1 crore", "previous_team": "SRH", "image": "https://example.com/shahbaz_ahamad_image"},
    {"name": "Moeen Ali", "base_price": "Rs 2 crore", "previous_team": "CSK", "image": "https://example.com/moeen_ali_image"},
    {"name": "Tim David", "base_price": "Rs 2 crore", "previous_team": "MI", "image": "https://example.com/tim_david_image"},
    {"name": "Deepak Hooda", "base_price": "Rs 75 lakh", "previous_team": "LSG", "image": "https://example.com/deepak_hooda_image"},
    {"name": "Will Jacks", "base_price": "Rs 2 crore", "previous_team": "RCB", "image": "https://example.com/will_jacks_image"},
    {"name": "Azmatullah Omarzai", "base_price": "Rs 1.5 crore", "previous_team": "GT", "image": "https://example.com/azmatullah_omarzai_image"},
    {"name": "R. Sai Kishore", "base_price": "Rs 75 lakh", "previous_team": "GT", "image": "https://example.com/r_sai_kishore_image"},
    {"name": "Romario Shepherd", "base_price": "Rs 1.5 crore", "previous_team": "MI", "image": "https://example.com/romario_shepherd_image"}
],

"Set 23: WKB1: Wicketkeeper Batsmen": [
    {"name": "Tom Banton", "base_price": "Rs 2 crore", "previous_team": "KKR", "image": "https://example.com/tom_banton_image"},
    {"name": "Sam Billings", "base_price": "Rs 1.5 crore", "previous_team": "CSK", "image": "https://example.com/sam_billings_image"},
    {"name": "Jordan Cox", "base_price": "Rs 1.25 crore", "previous_team": "Uncapped", "image": "https://example.com/jordan_cox_image"},
    {"name": "Ben McDermott", "base_price": "Rs 75 lakh", "previous_team": "Capped", "image": "https://example.com/ben_mcdermott_image"},
    {"name": "Kusal Mendis", "base_price": "Rs 75 lakh", "previous_team": "Capped", "image": "https://example.com/kusal_mendis_image"},
    {"name": "Kusal Perera", "base_price": "Rs 75 lakh", "previous_team": "RR", "image": "https://example.com/kusal_perera_image"},
    {"name": "Josh Philippe", "base_price": "Rs 75 lakh", "previous_team": "RCB", "image": "https://example.com/josh_philippe_image"},
    {"name": "Tim Seifert", "base_price": "Rs 1.25 crore", "previous_team": "KKR", "image": "https://example.com/tim_seifert_image"}
],



"Set 24: FA3 - Fast Bowlers": [
    {"name": "Nandre Burger", "base_price": "Rs 1.25 crore", "previous_team": "RR", "image": "https://example.com/nandre_burger_image"},
    {"name": "Spencer Johnson", "base_price": "Rs 2 crore", "previous_team": "GT", "image": "https://example.com/spencer_johnson_image"},
    {"name": "Umran Malik", "base_price": "Rs 75 lakh", "previous_team": "SRH", "image": "https://example.com/umran_malik_image"},
    {"name": "Mustafizur Rahman", "base_price": "Rs 2 crore", "previous_team": "CSK", "image": "https://example.com/mustafizur_rahman_image"},
    {"name": "Ishant Sharma", "base_price": "Rs 75 lakh", "previous_team": "DC", "image": "https://example.com/ishant_sharma_image"},
    {"name": "Nuwan Thushara", "base_price": "Rs 75 lakh", "previous_team": "MI", "image": "https://example.com/nuwan_thushara_image"},
    {"name": "Naveen Ul Haq", "base_price": "Rs 2 crore", "previous_team": "LSG", "image": "https://example.com/naveen_ul_haq_image"},
    {"name": "Jaydev Unadkat", "base_price": "Rs 1 crore", "previous_team": "SRH", "image": "https://example.com/jaydev_unadkat_image"},
    {"name": "Umesh Yadav", "base_price": "Rs 75 lakh", "previous_team": "Kolkata Knight Riders", "image": "https://example.com/umesh_yadav_image"}
],

"Set 25: SP3 - Spinners": [
    {"name": "Tabraiz Shamsi", "base_price": "Rs 2 crore", "previous_team": "RCB", "image": "https://example.com/tabraiz_shamsi_image"},
    {"name": "Jeffery Vandersay", "base_price": "Rs 75 lakh", "previous_team": "Sri Lanka", "image": "https://example.com/jeffery_vandersay_image"}
],

"Set 26: UBA3 - Uncapped All-rounders and Batters": [
    {"name": "Sachin Baby", "base_price": "Rs 75 lakh", "previous_team": "Uncapped", "image": "https://example.com/sachin_baby_image"},
    {"name": "Rajvardhan Hangargekar", "base_price": "Rs 75 lakh", "previous_team": "Uncapped", "image": "https://example.com/rajvardhan_hangargekar_image"},
    {"name": "Murugan Ashwin", "base_price": "Rs 75 lakh", "previous_team": "Uncapped", "image": "https://example.com/murugan_ashwin_image"},
    {"name": "Matthew Breetzke", "base_price": "Rs 75 lakh", "previous_team": "South Africa", "image": "https://example.com/matthew_breetzke_image"}
],

"Set 27: BA4 - Batsmen": [
    {"name": "Mark Chapman", "base_price": "Rs 1.5 crore", "previous_team": "New Zealand", "image": "https://example.com/mark_chapman_image"},
    {"name": "Brandon King", "base_price": "Rs 75 lakh", "previous_team": "West Indies", "image": "https://example.com/brandon_king_image"},
    {"name": "Evin Lewis", "base_price": "Rs 2 crore", "previous_team": "MI", "image": "https://example.com/evin_lewis_image"},
    {"name": "Pathum Nissanka", "base_price": "Rs 75 lakh", "previous_team": "Sri Lanka", "image": "https://example.com/pathum_nissanka_image"},
    {"name": "Bhanuka Rajapaksa", "base_price": "Rs 75 lakh", "previous_team": "PBKS", "image": "https://example.com/bhanuka_rajapaksa_image"},
    {"name": "Steve Smith", "base_price": "Rs 2 crore", "previous_team": "PWI", "image": "https://example.com/steve_smith_image"}
],

"Set 28: AL4 - All-Rounders": [
    {"name": "Gus Atkinson", "base_price": "Rs 2 crore", "previous_team": "KKR", "image": "https://example.com/gus_atkinson_image"},
    {"name": "Tom Curran", "base_price": "Rs 2 crore", "previous_team": "RCB", "image": "https://example.com/tom_curran_image"},
    {"name": "Krishnappa Gowtham", "base_price": "Rs 1 crore", "previous_team": "LSG", "image": "https://example.com/krishnappa_gowtham_image"},
    {"name": "Mohammad Nabi", "base_price": "Rs 1.5 crore", "previous_team": "MI", "image": "https://example.com/mohammad_nabi_image"},
    {"name": "Gulbadin Naib", "base_price": "Rs 1 crore", "previous_team": "DC", "image": "https://example.com/gulbadin_naib_image"},
    {"name": "Sikandar Raza", "base_price": "Rs 1.25 crore", "previous_team": "PBKS", "image": "https://example.com/sikandar_raza_image"},
    {"name": "Mitchell Santner", "base_price": "Rs 2 crore", "previous_team": "CSK", "image": "https://example.com/mitchell_santner_image"},
    {"name": "Jayant Yadav", "base_price": "Rs 75 lakh", "previous_team": "GT", "image": "https://example.com/jayant_yadav_image"}
],

"Set 29: WK4 - Wicketkeepers": [
    {"name": "Johnson Charles", "base_price": "Rs 75 lakh", "previous_team": "West Indies", "image": "https://example.com/johnson_charles_image"},
    {"name": "Litton Das", "base_price": "Rs 75 lakh", "previous_team": "KKR", "image": "https://example.com/litton_das_image"},
    {"name": "Andre Fletcher", "base_price": "Rs 75 lakh", "previous_team": "West Indies", "image": "https://example.com/andre_fletcher_image"},
    {"name": "Tom Latham", "base_price": "Rs 1.5 crore", "previous_team": "New Zealand", "image": "https://example.com/tom_latham_image"},
    {"name": "Ollie Pope", "base_price": "Rs 75 lakh", "previous_team": "England", "image": "https://example.com/ollie_pope_image"},
    {"name": "Kyle Verreynne", "base_price": "Rs 75 lakh", "previous_team": "South Africa", "image": "https://example.com/kyle_verreynne_image"}
],

"Set 30: FA4 - Fast Bowlers": [
    {"name": "Fazalhaq Farooqi", "base_price": "Rs 2 crore", "previous_team": "SRH", "image": "https://example.com/fazalhaq_farooqi_image"},
    {"name": "Richard Gleeson", "base_price": "Rs 75 lakh", "previous_team": "CSK", "image": "https://example.com/richard_gleeson_image"},
    {"name": "Matt Henry", "base_price": "Rs 2 crore", "previous_team": "LSG", "image": "https://example.com/matt_henry_image"},
    {"name": "Alzarri Joseph", "base_price": "Rs 2 crore", "previous_team": "RCB", "image": "https://example.com/alzarri_joseph_image"},
    {"name": "Kwena Maphaka", "base_price": "Rs 75 lakh", "previous_team": "MI", "image": "https://example.com/kwena_maphaka_image"},
    {"name": "Kuldeep Sen", "base_price": "Rs 75 lakh", "previous_team": "RR", "image": "https://example.com/kuldeep_sen_image"},
    {"name": "Reece Topley", "base_price": "Rs 75 lakh", "previous_team": "RCB", "image": "https://example.com/reece_topley_image"}
],

"Set 31: AL8 - All-Rounders": [
    {"name": "Lizaad Williams", "base_price": "Rs 1 crore", "previous_team": "SRH", "image": "https://example.com/lizaad_williams_image"},
    {"name": "Shakib Al Hasan", "base_price": "Rs 1 crore", "previous_team": "KKR", "image": "https://example.com/shakib_al_hasan_image"}
],

"Set 33: BA5 - Batters": [
    {"name": "Towhid Hridoy", "base_price": "Rs 75 lakh", "previous_team": "None", "image": "https://example.com/towhid_hridoy.jpg"},
    {"name": "Mikyle Louis", "base_price": "Rs 75 lakh", "previous_team": "None", "image": "https://example.com/mikyle_louis.jpg"},
    {"name": "Harry Tector", "base_price": "Rs 75 lakh", "previous_team": "None", "image": "https://example.com/harry_tector.jpg"},
    {"name": "Rassie Van Der Dussen", "base_price": "Rs 2 crore", "previous_team": "RR", "image": "https://example.com/rassie_van_der_dussen.jpg"},
    {"name": "Will Young", "base_price": "Rs 1.25 crore", "previous_team": "None", "image": "https://example.com/will_young.jpg"},
    {"name": "Najibullah Zadran", "base_price": "Rs 75 lakh", "previous_team": "None", "image": "https://example.com/najibullah_zadran.jpg"},
    {"name": "Ibrahim Zadran", "base_price": "Rs 75 lakh", "previous_team": "None", "image": "https://example.com/ibrahim_zadran.jpg"}
],
"Set 34: AL5 - All-Rounders": [
    {"name": "Sean Abbott", "base_price": "Rs 2 crore", "previous_team": "RCB,SRH", "image": "https://example.com/sean_abbott.jpg"},
    {"name": "Jacob Bethell", "base_price": "Rs 1.25 crore", "previous_team": "None", "image": "https://example.com/jacob_bethell.jpg"},
    {"name": "Brydon Carse", "base_price": "Rs 1 crore", "previous_team": "None", "image": "https://example.com/brydon_carse.jpg"},
    {"name": "Aaron Hardie", "base_price": "Rs 1.25 crore", "previous_team": "None", "image": "https://example.com/aaron_hardie.jpg"},
    {"name": "Sarfaraz Khan", "base_price": "Rs 75 lakh", "previous_team": "RCB,PBKS,DC", "image": "https://example.com/sarfaraz_khan.jpg"},
    {"name": "Kyle Mayers", "base_price": "Rs 1.5 crore", "previous_team": "LSG", "image": "https://example.com/kyle_mayers.jpg"},
    {"name": "Kamindu Mendis", "base_price": "Rs 75 lakh", "previous_team": "None", "image": "https://example.com/kamindu_mendis.jpg"},
    {"name": "Matthew Short", "base_price": "Rs 75 lakh", "previous_team": "PBKS", "image": "https://example.com/matthew_short.jpg"}
],
"Set 35: FA5 - Bowlers": [
    {"name": "Jason Behrendorff", "base_price": "Rs 1.5 crore", "previous_team": "CSK,RCB,MI", "image": "https://example.com/jason_behrendorff.jpg"},
    {"name": "Dushmantha Chameera", "base_price": "Rs 75 lakh", "previous_team": "RR,RCB,LSG,KKR", "image": "https://example.com/dushmantha_chameera.jpg"},
    {"name": "Nathan Ellis", "base_price": "Rs 1.25 crore", "previous_team": "PBKS", "image": "https://example.com/nathan_ellis.jpg"},
    {"name": "Shamar Joseph", "base_price": "Rs 75 lakh", "previous_team": "LSG", "image": "https://example.com/shamar_joseph.jpg"},
    {"name": "Josh Little", "base_price": "Rs 75 lakh", "previous_team": "GT", "image": "https://example.com/josh_little.jpg"},
    {"name": "Shivam Mavi", "base_price": "Rs 75 lakh", "previous_team": "KKR,GT,LSG", "image": "https://example.com/shivam_mavi.jpg"},
    {"name": "Jhye Richardson", "base_price": "Rs 1.5 crore", "previous_team": "PBKS,MI,DC", "image": "https://example.com/jhye_richardson.jpg"},
    {"name": "Navdeep Saini", "base_price": "Rs 75 lakh", "previous_team": "DC,RCB,RR", "image": "https://example.com/navdeep_saini.jpg"}

],

"Set 36: AL6 - All-Rounders": [
    {"name": "Qais Ahmad", "base_price": "Rs 75 lakh", "previous_team": "None", "image": "https://example.com/qais_ahmad.jpg"},
    {"name": "Charith Asalanka", "base_price": "Rs 75 lakh", "previous_team": "None", "image": "https://example.com/charith_asalanka.jpg"},
    {"name": "Michael Bracewell", "base_price": "Rs 1.5 crore", "previous_team": "RCB", "image": "https://example.com/michael_bracewell.jpg"},
    {"name": "Gudakesh Motie", "base_price": "Rs 75 lakh", "previous_team": "None", "image": "https://example.com/gudakesh_motie.jpg"},
    {"name": "Daniel Mousley", "base_price": "Rs 75 lakh", "previous_team": "None", "image": "https://example.com/daniel_mousley.jpg"},
    {"name": "Jamie Overton", "base_price": "Rs 1.5 crore", "previous_team": "None", "image": "https://example.com/jamie_overton.jpg"},
    {"name": "Dunith Wellalage", "base_price": "Rs 75 lakh", "previous_team": "None", "image": "https://example.com/dunith_wellalage.jpg"}
],
"Set 37: FA6 - Bowlers": [
    {"name": "Ottneil Baartman", "base_price": "Rs 75 lakh", "previous_team": "None", "image": "https://example.com/ottneil_baartman.jpg"},
    {"name": "Xavier Bartlett", "base_price": "Rs 75 lakh", "previous_team": "None", "image": "https://example.com/xavier_bartlett.jpg"},
    {"name": "Dilshan Madushanka", "base_price": "Rs 75 lakh", "previous_team": "MI", "image": "https://example.com/dilshan_madushanka.jpg"},
    {"name": "Adam Milne", "base_price": "Rs 2 crore", "previous_team": "RCB,MI,CSK", "image": "https://example.com/adam_milne.jpg"},
    {"name": "Lungisani Ngidi", "base_price": "Rs 1 crore", "previous_team": "CSK,DC", "image": "https://example.com/lungisani_ngidi.jpg"},
    {"name": "William O'Rourke", "base_price": "Rs 1.5 crore", "previous_team": "None", "image": "https://example.com/william_orourke.jpg"},
    {"name": "Chetan Sakariya", "base_price": "Rs 75 lakh", "previous_team": "RR,DC,KKR", "image": "https://example.com/chetan_sakariya.jpg"},
    {"name": "Sandeep Warrier", "base_price": "Rs 75 lakh", "previous_team": "None", "image": "https://example.com/sandeep_warrier.jpg"},
    {"name": "Wayne Parnell", "base_price": "Rs 1 crore", "previous_team": "PWI,DC,RCB", "image": "https://example.com/wayne_parnell.jpg"},
    {"name": "Keemo Paul", "base_price": "Rs 1.25 crore", "previous_team": "DC", "image": "https://example.com/keemo_paul.jpg"},
    {"name": "Odean Smith", "base_price": "Rs 1 crore", "previous_team": "None", "image": "https://example.com/odean_smith.jpg"}

],


"Set 38: AL7 - All-Rounders": [
    {"name": "Cooper Connolly", "base_price": "Rs 75 lakh", "previous_team": "None", "image": "https://example.com/cooper_connolly.jpg"},
    {"name": "Dushan Hemantha", "base_price": "Rs 75 lakh", "previous_team": "None", "image": "https://example.com/dushan_hemantha.jpg"},
    {"name": "Jason Holder", "base_price": "Rs 2 crore", "previous_team": "CSK,KKR,SRH,LSG,RR", "image": "https://example.com/jason_holder.jpg"},
    {"name": "Karim Janat", "base_price": "Rs 75 lakh", "previous_team": "None", "image": "https://example.com/karim_janat.jpg"},
    {"name": "Jimmy Neesham", "base_price": "Rs 1.5 crore", "previous_team": "DC,PBKS,MI,RR", "image": "https://example.com/jimmy_neesham.jpg"},
    {"name": "Daniel Sams", "base_price": "Rs 1.5 crore", "previous_team": "DC,RCB,MI,LSG", "image": "https://example.com/daniel_sams.jpg"},
    {"name": "William Sutherland", "base_price": "Rs 75 lakh", "previous_team": "None", "image": "https://example.com/william_sutherland.jpg"}
],
"Set 39: FA7 - Bowlers": [
    {"name": "Taskin Ahmed", "base_price": "Rs 1 crore", "previous_team": "None", "image": "https://example.com/taskin_ahmed.jpg"},
    {"name": "Ben Dwarshuis", "base_price": "Rs 75 lakh", "previous_team": "PBKS,DC", "image": "https://example.com/ben_dwarshuis.jpg"},
    {"name": "Obed McCoy", "base_price": "Rs 1.25 crore", "previous_team": "RR", "image": "https://example.com/obed_mccoy.jpg"},
    {"name": "Riley Meredith", "base_price": "Rs 1.5 crore", "previous_team": "None", "image": "https://example.com/riley_meredith.jpg"},
    {"name": "Lance Morris", "base_price": "Rs 1.25 crore", "previous_team": "None", "image": "https://example.com/lance_morris.jpg"},
    {"name": "Olly Stone", "base_price": "Rs 75 lakh", "previous_team": "None", "image": "https://example.com/olly_stone.jpg"}
],
"Set 40: AL8 - All-Rounders": [
    {"name": "Zak Foulkes", "base_price": "Rs 75 lakh", "previous_team": "None", "image": "https://example.com/zak_foulkes.jpg"},
    {"name": "Chris Green", "base_price": "Rs 1 crore", "previous_team": "KKR", "image": "https://example.com/chris_green.jpg"},
    {"name": "Shakib Al Hasan", "base_price": "Rs 1 crore", "previous_team": "SRH,KKR", "image": "https://example.com/shakib_al_hasan.jpg"},
    {"name": "Mehidy Hasan Miraz", "base_price": "Rs 1 crore", "previous_team": "None", "image": "https://example.com/mehidy_hasan_miraz.jpg"},
    {"name": "Wiaan Mulder", "base_price": "Rs 75 lakh", "previous_team": "None", "image": "https://example.com/wiaan_mulder.jpg"},
    {"name": "Dwaine Pretorius", "base_price": "Rs 75 lakh", "previous_team": "CSK", "image": "https://example.com/dwaine_pretorius.jpg"},
    {"name": "Dasun Shanaka", "base_price": "Rs 75 lakh", "previous_team": "GT", "image": "https://example.com/dasun_shanaka.jpg"}
],
"Set 41: FA8 - Bowlers": [
    {"name": "Shoriful Islam", "base_price": "Rs 75 lakh", "previous_team": "None", "image": "https://example.com/shoriful_islam.jpg"},
    {"name": "Blessing Muzarabani", "base_price": "Rs 75 lakh", "previous_team": "None", "image": "https://example.com/blessing_muzarabani.jpg"},
    {"name": "Matthew Potts", "base_price": "Rs 1.5 crore", "previous_team": "None", "image": "https://example.com/matthew_potts.jpg"},
    {"name": "Tanzim Hasan Sakib", "base_price": "Rs 75 lakh", "previous_team": "None", "image": "https://example.com/tanzim_hasan_sakib.jpg"},
    {"name": "Benjamin Sears", "base_price": "Rs 1 crore", "previous_team": "None", "image": "https://example.com/benjamin_sears.jpg"},
    {"name": "Tim Southee", "base_price": "Rs 1.5 crore", "previous_team": "CSK,RR,MI,RCB,KKR", "image": "https://example.com/tim_southee.jpg"}
],
"Set 42: FA9 - Bowlers": [
    {"name": "James Anderson", "base_price": "Rs 1.25 crore", "previous_team": "None", "image": "https://example.com/james_anderson.jpg"},
    {"name": "Kyle Jamieson", "base_price": "Rs 1.5 crore", "previous_team": "RCB,CSK", "image": "https://example.com/kyle_jamieson.jpg"},
    {"name": "Chris Jordan", "base_price": "Rs 2 crore", "previous_team": "RCB,SRH,PBKS,CSK,MI", "image": "https://example.com/chris_jordan.jpg"},
    {"name": "Hasan Mahmud", "base_price": "Rs 75 lakh", "previous_team": "None", "image": "https://example.com/hasan_mahmud.jpg"},
    {"name": "Tymal Mills", "base_price": "Rs 2 crore", "previous_team": "RCB,MI", "image": "https://example.com/tymal_mills.jpg"},
    {"name": "David Payne", "base_price": "Rs 1 crore", "previous_team": "None", "image": "https://example.com/david_payne.jpg"},
    {"name": "Nahid Rana", "base_price": "Rs 1 crore", "previous_team": "None", "image": "https://example.com/nahid_rana.jpg"}


]




}
teams = {}
unsold_players = []
bid_increment = 25_00_000
auction_duration = 23

# Random Auctioneer Statements
auctioneer_statements = [
    "The excitement is building up, folks! Who will take him home?",
    "We have a new bid! Who’s going to raise it?",
    "The bid is climbing, the crowd is buzzing!",
    "We’re at a critical point, do I hear another bid?",
    " Who’s going to claim him?",
    "The tension is high, and so is the bid!",
    "It’s getting intense, this is the moment for a bold move!"
    "Do I hear a bid?", "Who’s got the next bid?", "Don’t miss out on this one!", 
     "Someone’s about to steal this player!",
    "Any takers?", "Bid or miss your chance!","We’re heating up now!","We are getting close to the final call!",
    "Come on, ladies and gentlemen, this is a hot pick. Who’s going to take him home?","This player’s on fire this season! Do I hear another bid?",
    "Going up ! Who’s ready to take it to the next level?","Look at the stats, look at the potential! Who’s ready to secure this star?",
    "Don’t miss out on this one! A game-changer right here!","Alright, last chance! Do I see another raise before we close?",
    "Teams, it’s decision time – who’s taking him?",  "What an exciting bid! Let’s keep the momentum going!"


]



@bot.command(name="register_team")
async def register_team(ctx):
    team_options = [
        discord.SelectOption(label=team_data["name"], value=team_code, description=f"Purse: Rs {team_data['purse']:,}")
        for team_code, team_data in ipl_teams.items()
    ]
    select = Select(placeholder="Choose your IPL team!", options=team_options)
    view = View()
    view.add_item(select)
    embed = discord.Embed(title="Select Your IPL Team", description="Choose a team to register and begin the auction process.", color=discord.Color.green())
    await ctx.send(embed=embed, view=view)

    async def on_select(interaction: discord.Interaction):
        team_code = select.values[0]
        team_data = ipl_teams[team_code]
        if ctx.author.id in teams:
            await interaction.response.send_message("You have already registered a team.", ephemeral=True)
            return
        teams[ctx.author.id] = {
            "team_name": team_data["name"],
            "team_abbreviation": team_code,
            "purse": team_data["purse"],
            "players": team_data["retained_players"],
            "rtm_used": False
        }
        embed = discord.Embed(title="Team Registered", description=f"You've been registered with **{team_data['name']}**! Your purse is Rs {team_data['purse']:,}.", color=discord.Color.green())
        await interaction.response.send_message(embed=embed)

    select.callback = on_select

async def update_timer_embed(message, player, current_bid, current_bidder, time_left):
    embed = discord.Embed(
        title=f"🎉 Auction for {player['name']} 🎉",
        description=f"Current Bid: Rs {current_bid:,} by {current_bidder.name if current_bidder else 'No bids yet'}\nTime Left: {time_left} seconds",
        color=discord.Color.green() if current_bidder else discord.Color.blue()
    )
    embed.set_image(url=player["image"])
    await message.edit(embed=embed)


@bot.command(name="start_auction")
async def start_auction(ctx):
    if ctx.author.id not in teams:
        await ctx.send("Please register a team first using `!register_team`.")  # Ensure the user has registered a team.
        return

    await ctx.send("🎉 Welcome to the IPL Auction! 🎉")

    # Add Set Selection Menu at the start
    await display_set_selection_menu(ctx)

    while player_sets:
        # Wait for the user to select a set
        selected_set = await get_set_selection(ctx)
        if not selected_set:
            await ctx.send("⏳ Time out! No set selected. Please restart the auction.")
            return

        # Create the selection embed and start the auction for the chosen set
        confirm_embed = discord.Embed(
            title=f"⚡ Starting Auction for {selected_set} Set ⚡",
            description="Prepare to bid on the finest players!",
            color=discord.Color.orange()
        )
        await ctx.send(embed=confirm_embed)

        players = player_sets[selected_set]
        random.shuffle(players)

        # Auction each player in the chosen set
        for player in players:
            await auction_player(ctx, player)

        # Remove the completed set
        del player_sets[selected_set]

        if not player_sets:
            await ctx.send("🎉 All player sets have been auctioned! The auction is complete. 🎉")
        else:
            await ctx.send("✅ Set completed! Please select a new set to continue.")
            await display_set_selection_menu(ctx)  # Display set selection menu after completing a set


async def display_set_selection_menu(ctx):
    # Display available sets and prompt user for selection
    available_sets = list(player_sets.keys())
    options_message = "Please select a set to auction from the following:\n" + "\n".join(
        [f"{i + 1}. {set_name}" for i, set_name in enumerate(available_sets)]
    )
    await ctx.send(options_message)


async def get_set_selection(ctx):
    available_sets = list(player_sets.keys())

    def check(msg):
        return (
            msg.author == ctx.author
            and msg.channel == ctx.channel
            and msg.content.isdigit()
            and 1 <= int(msg.content) <= len(available_sets)
        )

    try:
        # Wait for the user to select a set
        msg = await bot.wait_for("message", check=check, timeout=60)
        selected_index = int(msg.content) - 1
        chosen_set = available_sets[selected_index]
        return chosen_set
    except asyncio.TimeoutError:
        return None



async def display_set_selection_menu(ctx):
    # Display available sets and prompt user for selection
    available_sets = list(player_sets.keys())
    options_message = "Please select a set to auction from the following:\n" + "\n".join(
        [f"{i + 1}. {set_name}" for i, set_name in enumerate(available_sets)]
    )
    await ctx.send(options_message)


async def get_set_selection(ctx):
    available_sets = list(player_sets.keys())

    def check(msg):
        return (
            msg.author == ctx.author
            and msg.channel == ctx.channel
            and msg.content.isdigit()
            and 1 <= int(msg.content) <= len(available_sets)
        )

    try:
        # Wait for the user to select a set
        msg = await bot.wait_for("message", check=check, timeout=60)
        selected_index = int(msg.content) - 1
        chosen_set = available_sets[selected_index]
        return chosen_set
    except asyncio.TimeoutError:
        return None



async def auction_player(ctx, player):
    base_price_str = player["base_price"].replace("Rs ", "")
    if "crore" in base_price_str:
        current_bid = int(float(base_price_str.replace(" crore", "")) * 1_00_00_000)
    elif "lakh" in base_price_str:
        current_bid = int(float(base_price_str.replace(" lakh", "")) * 1_00_000)
    current_bidder = None
    last_bidder = None  # Track the last person who placed a bid
    time_left = auction_duration

    embed = discord.Embed(
        title=f"🎉 Auctioning {player['name']} 🎉",
        description=f"**Base Price:** {player['base_price']}\n\n💸 Place your bids or use RTM rights if available!",
        color=discord.Color.blue()
    )
    embed.set_image(url=player["image"])
    embed.add_field(name="🏏 Previous Team", value=player["previous_team"], inline=True)
    embed.add_field(name="💰 Starting Bid", value=f"Rs {current_bid:,}", inline=True)
    embed.add_field(name="⌛ Time Left", value=f"{time_left} seconds", inline=True)
    embed.set_footer(text="Get ready to bid high and take home the star player!")

    auction_message = await ctx.send(embed=embed)

    bid_button = Button(label="💵 Place Bid", style=discord.ButtonStyle.green)
    rtm_button = Button(label="🔄 Use RTM", style=discord.ButtonStyle.primary)
    view = View()
    view.add_item(bid_button)

    async def bid_callback(interaction):
        nonlocal current_bid, current_bidder, time_left, last_bidder
        user_id = interaction.user.id
        team = teams.get(user_id)
        if not team:
            await interaction.response.send_message("Please register a team first.", ephemeral=True)
            return
        if team["purse"] < current_bid + bid_increment:
            await interaction.response.send_message("Insufficient funds.", ephemeral=True)
            return
        if last_bidder == interaction.user:
            await interaction.response.send_message("You can't place consecutive bids. Wait for another user to bid.", ephemeral=True)
            return

        current_bid += bid_increment
        current_bidder = interaction.user
        last_bidder = interaction.user  # Update the last bidder
        time_left = auction_duration

        auctioneer_speech = random.choice(auctioneer_statements)
        await ctx.send(f" **Auctioneer:** {auctioneer_speech}\nA New bid placed at **Rs {current_bid:,}** by ***{team['team_name']}!***")

        updated_embed = discord.Embed(
            title=f"🎉 Auctioning {player['name']} 🎉",
            description=f"**Current Bid:** Rs {current_bid:,} by **{current_bidder.name}**",
            color=discord.Color.gold()
        )
        updated_embed.set_image(url=player["image"])
        updated_embed.add_field(name="🏏 Previous Team", value=player["previous_team"], inline=True)
        updated_embed.add_field(name="💰 Current Bid", value=f"Rs {current_bid:,}", inline=True)
        updated_embed.add_field(name="⌛ Time Left", value=f"{time_left} seconds", inline=True)
        updated_embed.set_footer(text="Will you make the next move? Place your bid now!")
        await auction_message.edit(embed=updated_embed)

    bid_button.callback = bid_callback

    async def rtm_callback(interaction):
        user_id = interaction.user.id
        team = teams.get(user_id)
        if not team or player["previous_team"] != team["team_abbreviation"] or team["rtm_used"]:
            await interaction.response.send_message("RTM unavailable or already used.", ephemeral=True)
            return
        team["players"].append(player["name"])
        team["rtm_used"] = True
        await auction_message.delete()
        await ctx.send(f"🔄 RTM used! **{player['name']}** retained by **{team['team_name']}**.")

    rtm_button.callback = rtm_callback
    view.add_item(rtm_button)
    await auction_message.edit(view=view)

    while time_left > 0:
        await asyncio.sleep(1)
        time_left -= 1
        color = discord.Color.red() if time_left <= 10 else discord.Color.orange() if time_left <= 16 else discord.Color.green()
        embed.color = color
        embed.set_field_at(2, name="⌛ Time Left", value=f"{time_left} seconds", inline=True)
        await auction_message.edit(embed=embed)
    
    if current_bidder:
        user_id = current_bidder.id
        teams[user_id]["players"].append(player["name"])
        teams[user_id]["purse"] -= current_bid
        await ctx.send( f"**{player['name']}**[!](https://c.tenor.com/eIrPxV7DwCkAAAAd/tenor.gif) **sold to {teams[user_id]['team_name']}** for Rs {current_bid:,}.")

    else:
        unsold_players.append(player)
        await ctx.send(f"**{player['name']}** went unsold. No bids were placed.")


        
@bot.command(name="showplayers")
async def show_players(ctx):
    if ctx.author.id not in teams:
        await ctx.send("You must register a team first using `!register_team`.")  # Ensure the user has registered a team.
        return

    team = teams[ctx.author.id]
    team_name = team["team_name"]
    purse = team["purse"]
    retained_players = team["players"]
    
    # Create a message with retained players and their values (assuming all retained players are already in the team)
    player_list = "\n".join([f"**{player}** " for player in retained_players])
    
    # Show the team's purse balance
    balance_message = f"🎉 **{team_name}** 🎉\nPurse: Rs {purse:,}\n\nRetained Players:\n{player_list}"

    # Send the response message
    embed = discord.Embed(
        title=f"🔹 {team_name} Squad 🔹",
        description=balance_message,
        color=discord.Color.green()
    )
    await ctx.send(embed=embed)




@bot.command(name="purse")
async def purse(ctx):
    if ctx.author.id not in teams:
        await ctx.send("You must register a team first using `!register_team`.")
        return

    team = teams[ctx.author.id]
    embed = discord.Embed(
        title=f"💰 {team['team_name']}'s Purse 💰",
        description=f"Remaining Purse: Rs {team['purse']:,}",
        color=discord.Color.green()
    )
    await ctx.send(embed=embed)



@bot.command(name="show_teams")
async def show_all_teams(ctx):
    if not teams:
        await ctx.send("No teams have been registered yet.")
        return

    embed = discord.Embed(
        title="🌟 Team Squads and Purses 🌟",
        description="Here's the summary of all registered teams:",
        color=discord.Color.blue()
    )
    for team_id, team_data in teams.items():
        players = "\n".join(team_data["players"]) if team_data["players"] else "No players yet."
        embed.add_field(
            name=f"🔹 {team_data['team_name']} 🔹",
            value=f"💰 Purse: Rs {team_data['purse']:,}\n🏏 Players:\n{players}",
            inline=False
        )
    await ctx.send(embed=embed)





bot.run("MTMwNzY2MDc1Nzc4NTEyMDc3OA.GsFJWn.2MYwftudSxkaCgG8Ak96SxxhXmXZg4gX0KjKqo")