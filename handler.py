from random import choice
def response_handler(body):
    picture_list=[]
    message = ""
    if body == 'Start':
        message = "Welcome to the Mood Detector 2000! Please insert your mood."
        return (message, "0") 
    elif body == 'Happy':
        picture_list = ["https://upload.wikimedia.org/wikipedia/commons/7/75/Yuan_Zi_-_panda.jpg","https://nationalzoo.si.edu/Support/images/panda-conservation-hero.jpg", "https://aos.iacpublishinglabs.com/question/aq/1400px-788px/pandas-live_64dff22c2fe56e9.jpg?domain=cx.aos.ask.com", "http://i.kinja-img.com/gawker-media/image/upload/s--ft1APKVa--/18a5kzrhxhqwvjpg.jpg", "http://redpandanetwork.org/blog/wp-content/uploads/2014/06/GiantPandaEatingBamboo.jpg", "http://www.thedrinksbusiness.com/wordpress/wp-content/uploads/2013/05/pandas-640x425.jpg", "https://pandasaes.files.wordpress.com/2011/05/tww.jpeg" ] 
    elif body == 'Sad':
        picture_list = ["http://www.golden-retriever.com/wp-content/uploads/2015/06/cute-golden-retriever-happy-puppies.jpg", "http://www.gapviewkennel.com/wp-content/uploads/2012/05/golden-retriever-puppies_1-640x320.jpg", "http://www.passionforgold.com/Brown_1_op_800x800.jpg", "https://s-media-cache-ak0.pinimg.com/736x/af/56/14/af56140a532265db3e02168adfcdd857.jpg", "http://barkpost.com/wp-content/uploads/2015/05/Golden-Retriever-Puppy.jpg", "https://s3.amazonaws.com/s3.pupcity.com/_old/08019140622514_1.jpg", "http://www.labrador-retriever.club/images/labrador-retriever/golden-retriever-with-baby-puppy.jpg"]
    elif body == 'Angry':
        picture_list = ["http://kingofwallpapers.com/kitten/kitten-007.jpg", "http://i.telegraph.co.uk/multimedia/archive/02830/cat_2830677b.jpg", "https://www.hirerush.com/blog/wp-content/uploads/2016/02/playful-kitten-6683.jpg", "http://cdn3-www.cattime.com/assets/uploads/2011/08/best-kitten-names-1.jpg", "http://www.warrenphotographic.co.uk/photography/bigs/25280-Ginger-kitten-leaping-with-arms-outstretched-white-background.jpg", "https://pbs.twimg.com/profile_images/619573624903761920/EGZ2I6wG.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Lynx_kitten.jpg/1024px-Lynx_kitten.jpg"]
    elif body == 'Confused':
        picture_list = ["http://www.livescience.com/images/i/000/009/679/original/090511-platypus-02.jpg?interpolation=lanczos-none&downsize=*:1000", "http://www.zoo.org.au/sites/default/files/styles/zv_carousel_large/public/platypus-HS-animal-profile-web620.jpg?itok=vlgvXmwd", "http://www.slate.com/content/dam/slate/articles/health_and_science/wild_things/2015/06/150622_WILD_Platypus.jpg.CROP.promo-mediumlarge.jpg", "http://www.creationscience.com/onlinebook/webpictures/lifesciences-platypus.jpg", "http://www.zoo.org.au/sites/default/files/styles/zv_carousel_large/public/platypus-head-closeup-animal-profile-web620.jpg?itok=SMj_8PDO"]
    else:
        message = "Invalid command. Text 'start' to restart the Mood Dectector 2000."
    return choice (picture_list), "1"