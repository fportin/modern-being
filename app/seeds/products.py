from app.models import db, Product

# Adds a demo products, you can add other products here if you want
def seed_products():

    demo = [
        #Laptops
        Product(name='MacBook Pro 13”', 
                description="The Apple M1 chip gives the 13‑inch MacBook Pro speed and power beyond belief. With up to 2.8x CPU performance. Up to 5x the graphics speed. Apple's most advanced Neural Engine for up to 11x faster machine learning. And up to 20 hours of battery life — the longest of any Mac ever. It’s the most popular pro notebook, taken to a whole new level.",
                brand='Apple', 
                price=1499.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/laptops/MacBook-Pro-13.jpeg'
                ),
        Product(name='MacBook Pro 16”', 
                description="Designed for those who defy limits and change the world, the 16-inch MacBook Pro is by far the most powerful notebook Apple has ever made. With an immersive Retina display, superfast processors, advanced graphics, the largest battery capacity ever in a MacBook Pro, Magic Keyboard, and massive storage, it's the ultimate pro notebook for the ultimate user.",
                brand='Apple', 
                price=2799.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/laptops/MacBook-Pro-16.jpeg'
                ),        
        Product(name='MacBook Air', 
                description="Apple's thinnest, lightest notebook, completely transformed by the Apple M1 chip. CPU speeds up to 3.5x faster. GPU speeds up to 5x faster. With Apple's most advanced Neural Engine for up to 9x faster machine learning. The longest battery life ever in a MacBook Air. And a silent, fanless design. This much power has never been this ready to go.",
                brand='Apple', 
                price=1249.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/laptops/MacBook-Air.jpeg'
                ),        
        Product(name='Galaxy Book Pro 360', 
                description="Turn heads and turn around your work-life balance with the premium PC that converts to a top-of-the-line tablet. With a redesigned S Pen, a brilliant Super AMOLED screen, the latest Intel® 11th Gen Core™ processor, Intel® Evo™ certification and with Samsung's latest wi-fi chip, you get the power to flip from getting work done to fun instantly.",
                brand='Samsung', 
                price=1299.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/laptops/Galaxy-Book-Pro-360.jpg'
                ),        
        Product(name='Galaxy Book Flex2 Alpha', 
                description="Everything you love in a Galaxy PC, taken further. The ultra-slim Galaxy Book Flex2 ⍺ sits at the top of its class with a super vivid QLED touchscreen, the latest Intel® 11th Gen Core™ processor and a 2-in-1 design that transforms from a laptop to a tablet. With a super-fast-charging battery that lasts 18.5 hours¹ and innovations galore, this Galaxy Book was made to exceed all expectations.",
                brand='Samsung', 
                price=1049.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/laptops/Galaxy-Book-Flex2-Alpha.jpg'
                ),        
        Product(name='Galaxy Book Pro', 
                description="PC power that’s smartphone thin. Samsung's lightest Galaxy Book yet gives you a powerful Intel® 11th Gen Core™ processor, Intel® Evo™ certification, an advanced AMOLED screen and comes equipped with their latest wi-fi chip. Finish important projects, download huge files fast or watch movies in brilliant color. Discover the perfect mix of portability and productivity.",
                brand='Samsung', 
                price=1199.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/laptops/Galaxy-Book-Pro.jpg'
                ),        
        Product(name='XPS 15 Touch Laptop', 
                description="XPS laptops and 2-in-1s are precision crafted with premium materials, featuring stunning displays and the performance you demand to express your creative self and your big ideas.",
                brand='Dell', 
                price=2799.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/laptops/XPS-15-Touch-Laptop.jpeg'
                ),        
        Product(name='ALIENWARE X15 R1 GAMING LAPTOP', 
                description="With iconic designs, high-performance gaming and premium features, Alienware delivers the most immersive experiences.",
                brand='Dell', 
                price=3399.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/laptops/Alienware-x15-R1.jpeg'
                ),        
        Product(name='G5 15 5500', 
                description="G Series equips you with all the essentials you need to experience split-second responsiveness and immersive gameplay.",
                brand='Dell', 
                price=1269.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/laptops/Dell-G5-15-5500.jpeg'
                ),        
        Product(name='Surface Pro X', 
                description="With Microsoft SQ® 1 and new Microsoft SQ® 2 chipsets, blazing-fast LTE connectivity, their thinnest Surface features two USB-C® ports and a stunning, virtually edge-to-edge 13” touchscreen, plus new choice of colors. Surface Pro X Keyboard and rechargeable Surface Slim Pen sold separately.",
                brand='Microsoft', 
                price=1499.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/laptops/Surface-Pro-X.jpeg'
                ),        
        Product(name='Surface Book 3', 
                description="Meet the laptop that can handle your biggest demands. The most powerful Surface laptop yet combines speed, graphics, and immersive gaming with the versatility of a laptop, tablet, and portable studio. Feature's a high-resolution touchscreen.",
                brand='Microsoft', 
                price=3399.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/laptops/Surface-Book-3.jpeg'
                ),        
        Product(name='Surface Laptop 4', 
                description="Style and speed. Stand out on HD video calls backed by Studio Mics. Capture ideas on the vibrant touchscreen. Do it all with a perfect balance of sleek design, speed, immersive audio, and significantly longer battery life than before.",
                brand='Microsoft', 
                price=2399.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/laptops/Surface-Laptop-4.jpeg'
                ),        
        #Desktops
        Product(name='iMac 24”', 
                description="Say hello to the new iMac. Inspired by the best of Apple. Transformed by the M1 chip. Stands out in any space. Fits perfectly into your life.",
                brand='Apple', 
                price=1699.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/desktops/iMac-24”.jpeg'
                ),        
        Product(name='iMac 27”', 
                description="The 27‑inch iMac is packed with powerful tools and apps that let you take any idea to the next level. Its superfast processors and graphics, massive memory, and all-flash storage can tackle any workload with ease. And with its advanced audio and video capabilities and stunning 5K Retina display, everything you do is larger than life.",
                brand='Apple', 
                price=2299.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/desktops/iMac-27”.jpeg'
                ),        
        Product(name='Mac Pro', 
                description="Power to change everything. Say hello to a Mac that is extreme in every way. With the greatest performance, expansion, and configurability yet, it is a system created to let a wide range of professionals push the limits of what is possible.",
                brand='Apple', 
                price=5999.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/desktops/Mac-Pro.jpeg'
                ),        
        Product(name='Mac mini', 
                description="The Apple M1 chip takes their most versatile, do-it-all desktop into another dimension. With up to 3x faster CPU performance. Up to 6x faster graphics. And their most advanced Neural Engine for up to 15x faster machine learning. Get ready to work, play, and create on Mac mini with speed and power beyond anything you ever imagined.",
                brand='Apple', 
                price=899.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/desktops/Mac-mini.jpeg'
                ),        
        Product(name='Surface Studio 2', 
                description="The ultimate creative studio. Let your ideas flow with brilliant color, blazing graphics, faster processors, intuitive tools, and a stunning, adjustable 28” display.",
                brand='Microsoft', 
                price=3499.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/desktops/Surface-Studio-2.jpeg'
                ),        
        Product(name='XPS Desktop Special Edition', 
                description="Engineered and designed with purpose for ultimate power and expandability.",
                brand='Dell', 
                price=3279.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/desktops/XPS-Desktop-Special-Edition.jpeg'
                ),        
        Product(name='Inspiron 27 7000 Silver Touch All-In-One with A-Frame Stand', 
                description="Whether it's checking email, working on big projects, or safekeeping all your digital content, Inspiron desktops and all-in-ones keep you connected to what matters most.",
                brand='Dell', 
                price=1499.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/desktops/Inspiron-27-7000-Silver-Touch-All-In-One-with-A-Frame-Stand.jpg'
                ),        
        Product(name='ALIENWARE AURORA RYZEN™ EDITION R10 GAMING DESKTOP', 
                description="With iconic designs, high-performance gaming and premium features, Alienware delivers the most immersive experiences.",
                brand='Dell', 
                price=4819.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/desktops/ALIENWARE-AURORA-RYZEN™-EDITION-R10-GAMING-DESKTOP.jpg'
                ),        
        Product(name='HP ENVY 32 All-in-One PC', 
                description="Create without limits on the ENVY All-in-One PC's massive 32\" diagonal 4K UHD[2] display that features a high contrast display with a broad color gamut so you can bring you videos and photos projects to life like a pro at home. Experience the performance and responsiveness of the latest Octa-Core 10th Generation Intel® Core™ i7 processor and advanced NVIDIA® GeForce RTX™ 2070 dedicated graphics so you can create faster than ever.",
                brand='HP', 
                price=2299.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/desktops/HP-ENVY-32-All-in-One-PC.png'
                ),        
        Product(name='OMEN 30L Desktop GT13-0380t', 
                description="It’s gaming love at first sight. The OMEN 30L Desktop PC has got the looks and can back it up. With a power processor and graphics, you can play day one. And with being easy to upgrade and OMEN Gaming Hub, it’s crafted for the long term.",
                brand='HP', 
                price=3099.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/desktops/OMEN-30L-Desktop-GT13-0380t.png'
                ),        
        #Monitors
        Product(name='Pro Display XDR', 
                description="The first 32-inch Retina 6K display ever. Up to 1600 nits of brightness. An astonishing 1,000,000:1 contrast ratio and superwide viewing angle. Over a billion colors presented with exceptional accuracy. And dynamic range that transforms the professional workflow. Introducing Apple Pro Display XDR, the world’s best pro display.",
                brand='Apple', 
                price=5999.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/monitors/Pro-Display-XDR.jpeg'
                ),        
        Product(name='34" S65UA Ultra WQHD High Resolution Monitor with 1000R curvature and USB-C', 
                description="Feel fully immersed Ultra-WQHD resolution with 34\" curved display Immerse yourself in detail. Within games, movies or design projects, surround yourself with the 34\" ultra-wide curved display featuring a 21:9 aspect ratio. Ultra-WQHD provides the simplest way to maximize your screen real estate and experience truly seamless multitasking on just one screen.",
                brand='Samsung', 
                price=599.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/monitors/34-S65UA-Ultra-WQHD.jpg'
                ),        
        Product(name='49" CRG9 Dual QHD Curved QLED Gaming Monitor', 
                description="Equivalent to two 27-inch QHD displays side by side. Samsung's 49-inch CRG9 Curved QLED Gaming Monitor immerses you in detail and color. AMD Radeon FreeSync™ 2 technology and 120Hz refresh rate provide crisp images, even in fast motion scenes. A spectacle to behold, the 49-inch CRG9 is built to help you win more and do more.",
                brand='Samsung', 
                price=1199.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/monitors/49-CRG9-Dual-QHD.jpg'
                ),        
        Product(name='32" Odyssey G7 Gaming Monitor', 
                description="Make your gaming world, more lifelike than ever before. Packing in 1.7 times the pixel density of Full HD, WQHD resolution boasts incredibly detailed, pin-sharp images. Experience a fuller view with more space to take in all the action.",
                brand='Samsung', 
                price=799.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/monitors/32-Odyssey-G7.jpg'
                ),        
        Product(name='OMEN X Emperium 65-inch Big Format Gaming Monitor', 
                description="Brace for impact—because at-home gaming and entertainment will never be the same. With stunning 4K[1] HDR visuals, NVIDIA® G-SYNC® Ultimate[6] with blazing-fast refresh rates up to 144Hz[7], and built-in NVIDIA® SHIELD™, this cutting-edge display brings your entire living room to life. Game, stream entertainment, and lose yourself in a brilliant 64.5” diagonal screen—when it comes to immersion, it doesn’t get much bigger, or better, than this.",
                brand='HP', 
                price=4999.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/monitors/OMEN-X-Emperium-65-inch-Big-Format-Gaming-Monitor.png'
                ),        
        Product(name='HP Z43 42.5-inch 4K UHD Display', 
                description="Upgrade your impromptu meetings and collaborative brainstorming sessions with the 43” diagonal HP Z43 4K UHD Display. Get started immediately with single USB-C™ cable connectivity to your devices.",
                brand='HP', 
                price=764.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/monitors/HP-Z43-42.5-inch-4K-UHD-Display.png'
                ),        
        Product(name='OMEN X 27 240Hz Gaming Monitor', 
                description="Play at your full potential on a monitor that delivers frames at full-throttle speed. From edge to edge, this 240 Hz[1] monitor brings visuals to the next level, with HDR technology that delivers details and contrast like you've never seen before, so you’re ready to react fast, return fire, and rank up.",
                brand='HP', 
                price=584.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/monitors/OMEN-X-27-240Hz-Gaming-Monitor.png'
                ),        
        Product(name='38” UltraGear™ 21:9 Curved WQHD+ Nano IPS 1ms 144Hz HDR 400 Sphere Lighting 2.0 3-Side Virtually Borderless', 
                description="See your way to victory with the innovative 38GL950G-B UltraGear gaming monitor, providing the crispest visuals and the sharpest clarity. You can experience breath-taking immersion on a Nano IPS display with a 1ms response time.",
                brand='LG', 
                price=1599.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/monitors/38-UltraGear.jpeg'
                ),        
        Product(name='34" Class 21:9 UltraWide® 5K2K Nano IPS LED Monitor with HDR 600 (34" Diagonal)', 
                description="Multitaskers can now work in a generous 5:9 area while simultaneously viewing a 16:9 4K video on the same screen. The 5K2K 21:9 display of the 34WK95U offers 5120 x 2160 resolution optimized for video editors, programmers and developers, with convenient single-cable Thunderbolt® 3 connectivity.",
                brand='LG', 
                price=1499.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/monitors/34-Class-21-9-UltraWide.jpeg'
                ),        
        Product(name='32" Class UltraFine™ 4K UHD LED Monitor with Thunderbolt™ 3 (31.5" Diagonal)', 
                description="UHD 4K resolution displays breathtaking clarity and fine detail with four times the resolution of Full HD. Plus this monitor is designed to work with compatible calibration devices* that ensure precise adjustments of color, brightness and more.",
                brand='LG', 
                price=1299.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/monitors/32-Class-UltraFine.jpeg'
                ),        
        #Headphones
        Product(name='Bose Noise Cancelling Headphones 700', 
                description="Critically acclaimed for their powerful noise cancelling, astonishing sound, and unrivaled voice pickup, Bose Noise Cancelling Headphones 700 help turn any space into the perfect place to listen to music, get work done, or just shut out the world for a few moments and relax. So if you’re looking for the best wireless Bluetooth headphones for music and calls, you’ve found them.",
                brand='Bose', 
                price=379.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/headphones/Bose-Noise-Cancelling-Headphones-700.png'
                ),        
        Product(name='QuietComfort 35 wireless headphones II', 
                description="QuietComfort 35 wireless headphones II are engineered with renowned noise cancellation. With the Google Assistant and Amazon Alexa built-in, you have instant access to millions of songs, playlists and more—hands free.* Simply choose your voice assistant and ask away.",
                brand='Bose', 
                price=299.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/headphones/QuietComfort-35-wireless-headphones-II.png'
                ),        
        Product(name='Beoplay H95', 
                description="Celebrating 95 years of heritage in sound, design and craft excellence. Beoplay H95 is crafted for the ultimate listening experience with long lasting comfort and effective Active Noise Cancellation.",
                brand='Bang & Olufsen', 
                price=1350.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/headphones/Beoplay-H95.png'
                ),        
        Product(name='Beoplay H4', 
                description="Contemporary over-ear headphones with long-lasting comfort, superior sound and voice assistant.",
                brand='Bang & Olufsen', 
                price=300.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/headphones/Beoplay-H4.png'
                ),        
        Product(name='Amiron Wireless', 
                description="Home has always been considered the ideal place to experience your music. Now with the Amiron wireless, your music has the space to reach its full potential – and follow you wherever you go. Without cables. With best sound quality.",
                brand='Beyerdynamic', 
                price=549.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/headphones/Amiron-Wireless.png'
                ),        
        Product(name='Aventho Wireless', 
                description="Never has your favourite music sounded so perfect: the sound personalization of the high-end model Aventho wireless facilitates a new, personal listening experience. For musical enjoyment without any limits.",
                brand='Beyerdynamic', 
                price=299.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/headphones/Aventho-Wireless.png'
                ),        
        Product(name='GW100 v2', 
                description="The first and only open-back Bluetooth headphone on the market. No compromises… it's a Grado®. The GW100 v2 is the first Grado wireless headphone, featuring Bluetooth® technology. More than 25 years of experience designing the world's finest headphones naturally lead Grado Labs to developing the only open-back, Bluetooth headphone on the market. Some might think wireless and open-back are an odd pairing, but now you can enjoy audiophile quality sound untethered. Whether you're fly-fishing or just cleaning the gutters, you don't want wires dangling. But you do want awesome Grado sound. Grado's legendary driver technology, Bluetooth, padded headband, 40+ hour battery life, and a lightweight comfortable design make them perfect for today's portable lifestyle. The large soundstage and detail only available from an open-back design, plus Bluetooth, coalesces into the perfect wireless headphone.",
                brand='Grado', 
                price=249.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/headphones/GW100-v2.jpeg'
                ),        
        Product(name='Momentum 3 Wireless', 
                description="The new MOMENTUM Wireless is the latest addition to Sennheiser's ground-breaking, premium headphone range - offering superior sound, cutting-edge technology, and a modern design aesthetic to every moment. It redefines your premium headphone experience by reproducing the balanced depth and precision of studio-quality audio.",
                brand='Sennheiser', 
                price=349.95, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/headphones/Momentum-3-Wireless.jpg'
                ),        
        Product(name='RS 195', 
                description="Specialized wireless headphones. Personal and adaptable to your listening needs. With the RS 195, rediscover the pleasure of listening.",
                brand='Sennheiser', 
                price=449.95, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/headphones/RS-195.jpg'
                ),        
        Product(name='WH-1000XM4', 
                description="It’s just you and your music with the WH-1000XM4 headphones. The easy way to enjoy less noise and even purer sound, with smart listening technology that automatically personalises your experience.",
                brand='Sony', 
                price=298.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/headphones/WH-1000XM4.jpg'
                ),        
        #Smart Speakers
        Product(name='One (2nd Gen)', 
                description="Get rich, room-filling sound with Sonos One, and control it with your voice, the Sonos app, Apple AirPlay 2, and more.",
                brand='Sonos', 
                price=199.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/smart-speakers/One-2nd-Gen.png'
                ),        
        Product(name='Move', 
                description="Get brilliant sound anywhere with the weatherproof and drop-resistant Move. Control with your voice, the Sonos app, and Apple AirPlay 2 at home, and stream via Bluetooth® when WiFi isn't available.",
                brand='Sonos', 
                price=399.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/smart-speakers/Move.png'
                ),        
        Product(name='HomePod', 
                description="HomePod is a breakthrough speaker that adapts to its location and delivers high-fidelity audio wherever it’s playing. Together with Apple Music and Siri, it creates an entirely new way for you to discover and interact with music at home. And it can help you and your whole family with everyday tasks — and control your smart home — all with just your voice.",
                brand='Apple', 
                price=299.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/smart-speakers/Home-Pod.jpeg'
                ),        
        Product(name='HomePod mini', 
                description="Jam-packed with innovation, HomePod mini delivers unexpectedly big sound for a speaker of its size. At just 3.3 inches tall, it takes up almost no space but fills the entire room with rich 360‑degree audio that sounds amazing from every angle.",
                brand='Apple', 
                price=99.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/smart-speakers/HomePod-mini.jpeg'
                ),        
        Product(name='Echo (4th Gen)', 
                description="Talk about well-rounded. Echo combines premium sound, a built-in Zigbee smart home hub, and a temperature sensor. Powerful speakers deliver clear highs, dynamic mids, and deep bass for rich, detailed sound that adapts to any room.",
                brand='Amazon', 
                price=79.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/smart-speakers/Echo-4th-Gen.jpg'
                ),        
        Product(name='Echo Studio', 
                description="You've never heard an Echo like this before. Echo Studio creates an immersive, 3-dimensional soundscape, wrapping you in studio-quality audio from every direction.",
                brand='Amazon', 
                price=199.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/smart-speakers/Echo-studio.jpeg'
                ),        
        Product(name='Nest Audio', 
                description="Nest Audio adapts to your environment and whatever you’re listening to. So music sounds better. And news, radio, and audiobooks sound even clearer.",
                brand='Google', 
                price=99.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/smart-speakers/Nest-Audio.png'
                ),        
        Product(name='Nest Mini', 
                description="Nest Mini. Still mini. Even more mighty.",
                brand='Google', 
                price=34.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/smart-speakers/Nest-Mini.png'
                ),        
        Product(name='Bose Smart Speaker 500', 
                description="It’s powerfully simple. Fill any room with wall-to-wall stereo sound, while built-in voice control puts millions of songs at the tip of your tongue.",
                brand='Bose', 
                price=299.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/smart-speakers/Bose-Smart-Speaker-500.png'
                ),        
        Product(name='Bose Home Speaker 300', 
                description="The Bose Home Speaker 300 brings room-rocking bass and 360° lifelike sound to a space-saving size. Plus, with built-in voice assistants, like the Google Assistant and Alexa, all of your favorite music is just an ask away. Turn it up and feel the difference.",
                brand='Bose', 
                price=199.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/smart-speakers/Bose-Home-Speaker-300.png'
                ),        
        #Smart Watches
        Product(name='Apple Watch Series 6 (GPS) 44mm', 
                description="Apple Watch Series 6 lets you measure your blood oxygen level with a revolutionary new sensor and app. Take an ECG from your wrist. See your fitness metrics on the enhanced Always-On Retina display, now 2.5x brighter outdoors when your wrist is down. Set a bedtime routine and track your sleep. And reply to calls and messages right from your wrist. It’s the ultimate device for a healthier, more active, more connected life.",
                brand='Apple', 
                price=429.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/smart-watches/Apple-Watch-Series-6.jpeg'
                ),        
        Product(name='Apple Watch Nike SE (GPS) 44mm', 
                description="With Apple Watch Nike SE, you can track your workouts and listen to Audio Guided Runs with the Nike Run Club app. Sync music for motivation to your watch. Turn on Nike Twilight Mode for enhanced visibility. And choose from exclusive Nike watch faces and bands.",
                brand='Apple', 
                price=309.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/smart-watches/Apple-Watch-Nike-SE.jpeg'
                ),        
        Product(name='Fēnix 6X Pro Solar GPS/GLONASS/Galileo Watch', 
                description="Keep track of your fitness progress with this Garmin fenix 6X Pro Solar multisport GPS watch. The satellite navigation gives you the confidence to venture into paths less beaten, while the solar charging capability extends the battery life when outdoors. This Garmin fenix 6X Pro Solar multisport GPS watch features pace guidance assistance to keep you on your toes.",
                brand='Garmin', 
                price=849.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/smart-watches/Fēnix-6X-Pro-Solar-GPS:GLONASS:Galileo-Watch.jpeg'
                ),        
        Product(name='Fēnix 5 Sapphire GPS Smartwatch 47mm Fiber-Reinforced Polymer', 
                description="Ensure powerful performance by using this Fenix 5 sapphire watch. It monitors heart rate and location so that you can tell exactly how much exercise you've done, and it includes up to 24 hours of battery performance with the GPS on. Exceptional ruggedization combines with a sapphire lens to ensure this Fenix 5 sapphire watch resists daily abuse.",
                brand='Garmin', 
                price=749.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/smart-watches/Fēnix-5-Sapphire-GPS-Smartwatch-47mm-Fiber-Reinforced-Polymer.jpeg'
                ),        
        Product(name='Sense Advanced Health & Fitness Smartwatch', 
                description="Meet Fitbit Sense--the advanced health smartwatch that helps you tune into your body and guides you toward better health. Assess your heart for AFib right from your wrist, detect and manage stress, better understand your sleep quality and even keep an eye on patterns in your skin temperature or well-being with SpO2. Plus, Sense unlocks a 6-month trial of personalized guidance and advanced insights for new Fitbit Premium users.",
                brand='Fitbit', 
                price=249.95, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/smart-watches/Sense-Advanced-Health-&-Fitness-Smartwatch.jpeg'
                ),        
        Product(name='Versa 3 Health & Fitness Smartwatch', 
                description="Meet Fitbit Versa 3--the smartwatch with everything you need to just go. Track your pace & distance--and leave your phone at home--with built-in GPS. You can also get call, text and app notifications, use Google Assistant or Amazon Alexa Built-in and control Spotify, Deezer and Pandora when your phone is nearby.* Plus with Active Zone Minutes, 20+ exercise modes and 6+ day battery with 12-minute fast charging, you've got all the motivation you need to reach your health & fitness goals.(Notifications work when your phone is nearby. Voice assistant not available in all countries, see fitbit.com/voice. Subscriptions required for use of music services; not available in all countries.Battery life varies with use and other factors; up to 12 hours with continuous GPS. 12-minute fast charging adds 24 hours of battery life)",
                brand='Fitbit', 
                price=199.95, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/smart-watches/Versa-3-Health-&-Fitness-Smartwatch.jpeg'
                ),        
        Product(name='Galaxy Watch3 Smartwatch 45mm Stainless LTE', 
                description="The most advanced Samsung smartwatch is now also the most stylish. The Galaxy Watch3 combines powerful technology with a premium, customizable design so you can manage the day-today from your wrist, beautifully. With LTE connection, call, text and pay from your watch so you can leave your phone behind while you run out for coffee or go run a 5K. Keep an eye on wellness with advanced health monitoring, and go for days without charging.",
                brand='Samsung', 
                price=479.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/smart-watches/Galaxy-Watch3-Smartwatch-45mm-Stainless-LTE.jpg'
                ),        
        Product(name='Gear S3 Classic Smartwatch 46mm Stainless Steel', 
                description="Bring the classic style of a watch into the 21st century with this Samsung Gear S3 Classic smartwatch. Ease of use combines with smart aesthetics to make it simple to operate, and the ultralong battery life means you won't have to charge it for days. Keep track of all your stats with ease using this Samsung gear S3 Classic smartwatch.",
                brand='Samsung', 
                price=399.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/smart-watches/Gear-S3-Classic-Smartwatch-46mm-Stainless-Steel.jpg'
                ),        
        Product(name='Fossil - Gen 5 LTE Smartwatch (Cellular) 45mm', 
                description="Tech for real life. This 45mm Gen 5 LTE touchscreen smartwatch features a black silicone strap, phone-free calling functionality, 8GB storage capacity and three smart battery modes to extend battery life for multiple days. Fossil Gen 5 LTE smartwatches work exclusively with Verizon branded Android phones (not unlocked phones) on the Verizon Network with qualified Numbershare data plan. NumberShare is required to activate service on LTE smartwatches. Numbershare is available with an eligible Verizon monthly plan. Adding a smartwatch to your Verizon data plan will incur additional monthly charges. Customers must have a compatible Android Smartphone (4G or 5G) active on their Verizon account. Compatible Android smartphone must have OS 6.0 or later, excluding Go edition, with an updated version of the MVS app \"My Verizon Services\" (v.1.0.104.2 or later) and must be HD voice capable, have HD voice turned On and be on an eligible plan. LTE smartwatches do not support a standalone activation, only activation via NumberShare is eligible. For more detailed information, please refer to your Verizon Connected Devices plan. Fossil Gen 5 LTE Smartwatches powered with Wear OS by Google are only compatible with Verizon Android™ phones on the Verizon network. Wear OS by Google and other related marks are trademarks of Google LLC. Supported features may vary between platforms. To avoid damage to your watch, only use with included charger. Do not use a USB hub, USB splitter, USB y-cable, battery pack or other peripheral device to charge. Product should be kept more than 20cm away from implanted medical devices to minimize potential for RF interference. See product insert for full details.",
                brand='Fossil', 
                price=349.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/smart-watches/Fossil-Gen-5-LTE-Smartwatch.jpeg'
                ),        
        Product(name='Fossil - Gen 5e Smartwatch 44mm Leather', 
                description="Tech for real life. This 44mm Gen 5E touchscreen smartwatch features a smoke case and brown leather strap, speaker functionality, 4GB storage capacity and three smart battery modes to extend battery life for multiple days. Smartwatches powered with Wear OS by Google are compatible with iPhone® and Android™ phones. Wear OS by Google and other related marks are trademarks of Google LLC. Supported features may vary between platforms. To avoid damage to your watch, only use with included charger. Do not use a USB hub, USB splitter, USB y-cable, battery pack or other peripheral device to charge. Product should be kept more than 20cm away from implanted medical devices to minimize potential for RF interference. See product insert for full details.",
                brand='Fossil', 
                price=244.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/smart-watches/Fossil-Gen-5e-Smartwatch-44mm-Leather.jpeg'
                ),        
        #Smart Phones
        Product(name='iPhone 12 Pro Max', 
                description="5G goes Pro. A14 Bionic rockets past every other smartphone chip. The Pro camera system takes low-light photography to the next level — with an even bigger jump on iPhone 12 Pro Max. And Ceramic Shield delivers four times better drop performance. Let’s see what this thing can do.",
                brand='Apple', 
                price=1099.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/smart-phones/iPhone-12-Pro-Max.jpeg'
                ),        
        Product(name='iPhone 12', 
                description="5G speed. A14 Bionic, the fastest chip in a smartphone. An edge-to-edge OLED display. Ceramic Shield with four times better drop performance. And Night mode on every camera. iPhone 12 has it all — in two perfect sizes.",
                brand='Apple', 
                price=799.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/smart-phones/iPhone-12.jpeg'
                ),        
        Product(name='Galaxy Z Fold2 5G', 
                description="A mind-bending glass screen that folds like a book. A hands-free camera that shoots when you wave. A precision crafted hinge that transforms a cutting-edge smartphone into something much more. Meet the anything but ordinary Galaxy Z Fold2 5G.",
                brand='Samsung', 
                price=1199.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/smart-phones/Galaxy-Z-Fold2-5G.jpg'
                ),        
        Product(name='Galaxy S21 Ultra 5G', 
                description="Introducing Galaxy S21 Ultra 5G. The highest resolution photos and video on a smartphone. Galaxy's fastest processor yet. A battery that goes all-day—and then some. First ever S Pen compatibility. A striking new design. It's an Ultra that easily lives up to its name.",
                brand='Samsung', 
                price=1249.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/smart-phones/Galaxy-S21-Ultra5G.jpg'
                ),        
        Product(name='Pixel 5 5G 128GB', 
                description="What happens when you bring together the ultimate Google phone and the speed of 5G?* You get Pixel 5. The super fast Google phone at a helpful price.",
                brand='Google', 
                price=649.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/smart-phones/Pixel-5-5G-128GB.jpeg'
                ),        
        Product(name='Pixel 4a 5G UW 128GB', 
                description="Pixel 4a with 5G is the budget-friendly, super fast phone from Google. It has the helpful stuff you need in a phone, with an extra boost of 5G speed.",
                brand='Google', 
                price=499.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/smart-phones/Pixel-4a-5G-UW-128GB.jpeg'
                ),        
        Product(name='V40 ThinQ - Aurora Black', 
                description="Capture moments at different angles with this Verizon LG V40 ThinQ smartphone. The five-camera design offers multiple ways to take selfies and other photos, and the 6.4-inch display lets you view them clearly in vibrant colors. This LG V40 ThinQ smartphone has a Boombox speaker so you can enjoy DTS:X surround sound wherever you go.",
                brand='LG', 
                price=879.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/smart-phones/V40-ThinQ-Aurora-Black.jpeg'
                ),        
        Product(name='G8X ThinQ - Aurora Black', 
                description="LG G8X ThinQ Cell Phone for AT&T: Do more at once with this LG G8X ThinQ smartphone. The 6.4-inch OLED FullVision display connects to a detachable secondary display to create a foldable dual-screen experience, while the 32.0MP front camera lets you capture favorite moments. This LG G8X ThinQ smartphone features a Snapdragon 855 processor, 6GB of RAM and 128GB storage for seamless performance.",
                brand='LG', 
                price=779.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/smart-phones/G8X-ThinQ-Aurora-Black.jpeg'
                ),        
        Product(name='Xperia 1 II 256GB', 
                description="Stay connected with this unlocked Sony Xperia 1 II smartphone. The 6.5-inch 4K OLED HDR screen delivers detailed visuals and easy menu navigation, while the octa-core Qualcomm Snapdragon processor and 8GB of RAM provide fast processing speeds. This black Sony Xperia 1 II smartphone has 256GB of built-in storage to hold files and applications, and the triple 12.0MP camera lets you capture stunning, clear photos.",
                brand='Sony', 
                price=1149.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/smart-phones/Xperia-1-II-256GB.jpeg'
                ),        
        Product(name='Xperia 5 II 128GB', 
                description="Level up your entertainment and creativity with a 120Hz 21:9 CinemaWide™ 6.1” HDR OLED display and technology from Sony´s audio, video and award-winning Alpha camera series. Featuring one front facing 8MP camera and three 12MP rear cameras with ZEISS® optics, Real-time Eye AF, up to 20fps with AF/AE tracking and Photography Pro with RAW lets you capture stunning images in almost any lighting condition. It also has the world’s first 4K HDR 120fps slow-motion movie recording in a smartphone. High-Resolution Audio, a 3.5mm audio jack and front-facing stereo speakers deliver incredible sound. The 120Hz refresh rate and 240Hz touch scanning rate gives you the smoothest and most accurate gaming experience. All these features driven by the Qualcomm®12 Snapdragon™ 865 processor with 4G speed and Android 10, in a slim, compact and beautiful design that easily fits in a pocket.",
                brand='Sony', 
                price=899.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/smart-phones/Xperia-5-II-128GB.jpeg'
                ),        
        #Tablets
        Product(name='iPad Pro', 
                description="The ultimate iPad experience. Now with breakthrough M1 performance, a breathtaking XDR display, and blazing‑fast 5G wireless. Buckle up.",
                brand='Apple', 
                price=1099.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/tablets/iPad-Pro.png'
                ),        
        Product(name='iPad Air', 
                description="iPad Air does more than a computer in simpler, more magical ways. And now with more features and capabilities, it’s more versatile than ever.",
                brand='Apple', 
                price=749.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/tablets/iPad-Air.jpeg'
                ),        
        Product(name='iPad', 
                description="The new iPad combines tremendous capability with unmatched ease of use and versatility. With the powerful A12 Bionic chip, support for Apple Pencil and the Smart Keyboard, and the amazing new things you can do with iPadOS 14, now there’s even more to love about iPad.",
                brand='Apple', 
                price=459.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/tablets/iPad.jpeg'
                ),        
        Product(name='Galaxy Tab S7+, 128GB', 
                description="Get immersed on the Tab S7+'s  amazing 12.4 inch Super AMOLED and the 120Hz refresh rate for smooth viewing experiences.Rich audio and 3D surround sound with Quad speakers by AKG and Dolby ATMOS. Plus, the biggest leap in S Pen responsiveness for true writing experience.",
                brand='Samsung', 
                price=1049.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/tablets/Galaxy-Tab-S7-plus.jpg'
                ),        
        Product(name='Galaxy Tab A 10.1, 128GB', 
                description="Minimal bezel. Maximum view. Watch, stream and browse on a 10.1\" Full HD corner-to-corner display. Big sound for big entertainment. The perfect complement to a wide, immersive picture, Dolby Atmos surround sound fills the room with cinematic clarity.",
                brand='Samsung', 
                price=329.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/tablets/Galaxy-Tab-A-10.1,128GB.jpg'
                ),        
        Product(name='Galaxy Tab S7, 256GB', 
                description="Get immersed in the Tab S7's 11 inch screen and the 120Hz refresh rate for smooth viewing experiences. Rich audio and 3D surround sound with Quad speakers by AKG and Dolby ATMOS. Plus, the biggest leap in S Pen responsiveness for true writing experience.",
                brand='Samsung', 
                price=649.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/tablets/Galaxy-Tab-S7,-256GB.jpg'
                ),        
        Product(name='Surface Pro 7 - 12.3" Touch Screen - Intel Core i5 - 8GB Memory - 256GB SSD', 
                description="At your desk, on the couch, or out in the yard, Surface Pro 7 adapts to the way you work with laptop-to-tablet versatility. And now, it delivers more power than ever, with a laptop-class Intel® Core™ processor, all-day battery¹, Instant On, and improved graphics — plus more multitasking connections, including both USB-C® and USB-A ports.",
                brand='Microsoft', 
                price=1199.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/tablets/Surface-Pro-7-12.3.jpeg'
                ),        
        Product(name='Surface Go 2 - 10.5" Touch-Screen - Intel Core M - 8GB - 128GB SSD - WiFi + 4G LTE', 
                description="Your perfect everyday companion. New 10.5\" Surface Go 2 is perfect for keeping up and winding down - delivering tablet portability with laptop versatility, long battery life, a stunning touchscreen, and Windows security for the whole family. Browse, shop, and manage email with ease, relax with your favorite TV shows, and much more.",
                brand='Microsoft', 
                price=729.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/tablets/Surface-Go-2-10.5.jpeg'
                ),        
        Product(name='Kindle Oasis E-Reader + Cellular - 7" - 32GB', 
                description="Indulge your inner bookworm with this 32GB AT&T Amazon Kindle Oasis e-reader. The backlit touchscreen with adjustable warm light provides a realistic reading experience, and the intuitive interface makes it easy to find new books to read. Integrated WAN and Bluetooth 4.1 connectivity lets this Amazon Kindle Oasis e-reader download titles and stream Audible audiobooks to wireless headphones.",
                brand='Amazon', 
                price=349.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/tablets/Kindle-Oasis-E-Reader.jpeg'
                ),        
        Product(name='Wacom - Cintiq Pro 24 – 23.6” 4K Creative Pen and Touch Display', 
                description="Generate the highest quality art with this Wacom Cintiq Pro 24-inch tablet. Every movement and pressure change of your hand is flawlessly captured by the pen technology, and colors come to life on the 4K screen. The natural tilt support ensures a realistic writing experience on this Wacom Cintiq Pro 24-inch tablet.",
                brand='Wacom', 
                price=2499.95, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/tablets/Wacom-Cintiq-Pro-24–23.6”-4K-Creative-Pen-and-Touch-Display.jpeg'
                ),        
        #AR/VR Glasses
        Product(name='Quest 2 — Advanced All-In-One Virtual Reality Headset', 
                description="Oculus Quest 2 is our most advanced all-in-one VR system yet. Every detail has been engineered to make virtual worlds adapt to your movements, letting you explore awe-inspiring games and experiences with unparalleled freedom. No PC or console required. Get the most out of each moment with blazing-fast performance and next-generation graphics. Stay focused with a stunning display that features 50% more pixels than the original Quest. Or take a break from the action and grab front-row seats to live concerts, exclusive events and more. The redesigned Touch controllers feature improved ergonomics and intuitive controls that transport your gestures, motions and actions directly into VR. You can even connect your VR headset to a gaming-compatible computer with an Oculus Link cable to access hundreds of PC VR games and experiences. Quest 2 also lets you bring your friends into the action. With live casting, you can share your VR experience with people around you. Or meet up with friends in virtual worlds to battle in multiplayer competitions or just spend some time together. With Oculus Quest 2, there’s no end in sight to what you can play, create and discover in virtual reality.",
                brand='Oculus', 
                price=399.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/ar:vr-glasses/Quest-2-Advanced-All-In-One-Virtual-Reality-Headset.jpg'
                ),        
        Product(name='Lenovo Star Wars', 
                description="The smartphone-powered augmented reality experience brings an all-new Star Wars experience right into your home. Start the app, put on the headset, and begin your journey with three epic experiences. Wield a lightsaber and villains, train yourself in strategic combat against invading forces, and master the strategy of intergalactic Holochess",
                brand='Lenovo', 
                price=165.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/ar:vr-glasses/Lenovo-Star-Wars.jpg'
                ),        
        Product(name='HoloLens 2', 
                description="HoloLens 2 offers the most comfortable and immersive mixed reality experience available-enhanced by the reliability, security, and scalability of Azure.",
                brand='Microsoft', 
                price=3500.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/ar:vr-glasses/HoloLens2.png'
                ),        
        Product(name='dynaEdge', 
                description="The dynaEdge™ AR Smart Glasses enable multiple usage scenarios, including See-What-I-See, Remote Expert, Document Retrieval, Workflow Instructions and Real-Time Data Capture, making it the enterprise solution for tomorrow—starting today.",
                brand='Toshiba', 
                price=1899.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/ar:vr-glasses/dynaEdge.png'
                ),        
        Product(name='Raptor', 
                description="Raptor is the world’s first cycling computer for people, not bikes. Raptor is designed to enhance every ride by projecting an unobtrusive AR layer of information out in front of the cyclist’s eyes. Having real-time information projected out in front of you allows you to keep your eyes on the road ahead – increasing safety while focusing on performance, body posture, and accomplishments or simply soaking in the views and enjoying an amazing bike ride. Raptor’s HD front-facing camera allows you to relive your unforgettable moments with real-time metrics embedded in the videos.",
                brand='Everysight', 
                price=599.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/ar:vr-glasses/Raptor.png'
                ),        
        Product(name='Magic Leap 1', 
                description="Magic Leap 1 is a lightweight, wearable computer that seamlessly blends the digital and physical worlds, allowing digital content to coexist with real world objects and the people around you. It sees what you see and uses its understanding of surroundings and context to create unbelievably believable experiences.",
                brand='Magic Leap', 
                price=2295.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/ar:vr-glasses/Magic-Leap-1.png'
                ),        
        Product(name='Moverio BT-40S Smart Glasses with Intelligent Touch Controller', 
                description="Offering outstanding image quality and an intuitive touch controller, Epson Moverio BT-40S smart glasses take AR applications to the next level. Featuring innovative Si-OLED technology and dual-binocular displays – all in a comfortable design, they're the next generation of wearable, second-screen solutions.",
                brand='Epson', 
                price=999.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/ar:vr-glasses/Moverio-BT-40S-Smart-Glasses-with-Intelligent-Touch-Controller.jpeg'
                ),        
        Product(name='Glass', 
                description="Glass is a small, lightweight wearable computer with a transparent display for hands-free work.",
                brand='Google', 
                price=1167.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/ar:vr-glasses/Glass-2.jpg'
                ),        
        Product(name='X2 Mixed Reality Glasses', 
                description="Lightweight mixed reality glasses. At 9.8 ounces, the X2 Mixed Reality Glasses fit a wide field of view, contain powerful sensors, and come with the VisionEye SLAM SDK into an exceptionally minimalistic form factor.",
                brand='ThirdEye', 
                price=1950.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/ar:vr-glasses/X2-Mixed-Reality-Glasses.png'
                ),        
        Product(name='Spectacles 3', 
                description="Capture your world in 3D. Relive it with your 3D Viewer.",
                brand='Snap', 
                price=380.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/ar:vr-glasses/Spectacles-3.jpg'
                ),        
        #Gesture & Immersion
        Product(name='Kai Gesture Controller', 
                description="The KAI is an intuitive device capable of tracking the slightest movements of your wrist and all four fingers to recognize gestures. It then processes these gestures on-board, allowing you to interact with your digital world easily. Virtual reality, Gaming, Presentations, Hardware Control & so on… The applications of the Kai are virtually endless.",
                brand='Vicara', 
                price=150.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/gesture&immersion/Kai-Gesture.png'
                ),        
        Product(name='NeoRhythm', 
                description="NeoRhythm is a wearable technology using PEMF to entrain your brain. It has multiple programs for improved sleep, theta meditation, deep relaxation, improved focus, pain control, enhancing mental capacity, and energy and vitality.",
                brand='OmniPEMF', 
                price=299.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/gesture&immersion/NeoRhythm.jpeg'
                ),        
        Product(name='CaptoGlove Wireless Virtual Reality Glove for Gaming and Smart Devices', 
                description="CaptoGlove is a smart controller with advanced technology to precisely detect a wide variety of hand and finger movements. These gestures are translated into control commands which are sent directly to connected devices (such as PCs, VR Headsets, Smart Home, Internet of Things, iOS/Android Phones/Tablets/Consoles) to interact and control them faster, more naturally, and effectively. One glove can be used as a single controller or coupled with another CaptoGlove for use as a pair via a Bluetooth Low Energy (BTLE).",
                brand='CaptoGlove', 
                price=490.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/gesture&immersion/CaptoGlove-Wireless-VR&Smart-Devices.jpeg'
                ),        
        Product(name='TACTIGON Skin Developer Kit', 
                description="Tactigon SKIN is a programmable wearable to enable gesture control for robots, PC games, VR/AR, computers, 3D printers, drones, apps, and more.",
                brand='THE TACTIGON', 
                price=800.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/gesture&immersion/TACTIGON-Skin.jpeg'
                ),        
        Product(name='TeraRanger Evo Swipe Plus', 
                description="Detect people movement, trigger actions based on proximity, understand customer engagement and perform touchless gesture recognition with one compact ToF sensor.",
                brand='Terabee', 
                price=129.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/gesture&immersion/TeraRanger-Evo-Swipe-Plus.jpeg'
                ),        
        Product(name='Neeuro’s Revolutionary Brainwave-Sensing Headband for Everyone', 
                description="As stated by the World Health Organization (WHO), “there is no health without mental health.” When Neeuro first started, we envisioned ourselves creating something that would free people from their fear of early cognitive decline. We’ve seen family & friends slowing down and feeling isolated, and we thought, surely there must be a better way to age gracefully. After years of extensive R&D, we’ve developed a solution that gives both young and old the platform to nurture, develop, and maintain cognitive performance and mental health.",
                brand='Neeuro', 
                price=279.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/gesture&immersion/Neeuro’s-Revolutionary-Brainwave-Sensing-Headband.jpeg'
                ),        
        Product(name='Elf Emmit - Improve Focus, Sleep, Meditation and Learning Processes', 
                description="ELF emmit is a digital metronome which you control, choosing your preferred state of mind AND BODY by allowing the device to suggest how your mind should behave and the rhythm at which it operates. Elf emmit is a personal assistant which coaxes our minds and bodies to work as we would like them to.",
                brand='Elf Emmit', 
                price=199.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/gesture&immersion/Elf-Emmit.jpeg'
                ),        
        Product(name='Pegasi Glasses', 
                description="PEGASI glasses is our first “closed-loop” sleep quality optimization product. By analysis of big data from different human groups on the Health Cloud platform, customized and personalized sleep quality improving protocols are offered.",
                brand='Pegasi', 
                price=299.00, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/gesture&immersion/Pegasi-Glasses.png'
                ),        
        Product(name='Muse S', 
                description="Using advanced EEG technology to respond to your mind, heart, and breath, the Muse S is a comfy brain sensing headband that helps you understand and track how well you focus, sleep and recharge so you can refocus during the day and recover each night.",
                brand='Muse', 
                price=349.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/gesture&immersion/Muse-S.jpg'
                ),        
        Product(name='Muse 2', 
                description="Muse 2 is a multi-sensor meditation device that provides real-time feedback on your brain activity, heart rate, breathing, and body movements to help you build a consistent meditation practice.",
                brand='Muse', 
                price=249.99, 
                photo='https://modern-being.s3.us-west-2.amazonaws.com/gesture&immersion/Muse-2.jpg'
                )        
                ]

    [db.session.add(item) for item in demo]

    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and resets
# the auto incrementing primary key
def undo_products():
    db.session.execute('TRUNCATE products RESTART IDENTITY CASCADE;')
    db.session.commit()
