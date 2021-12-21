from project import Project, ProjectImgs

from staticjinja import Site

projects = [
    Project(
        name='EF Cash Carry Tool',
        description='Developed a proof-of-concept WinForms application, written in C#, to automate regular tasks at work by parsing pdf documents and using the data to generate new pdf documents, this allowed the tasks to be done in less than a quarter of the previous time.',
        context='Independent',
        git_link='https://github.com/aaron29th/EF_Cash_Carry_Tool',
        images=ProjectImgs(
            id='efCashCarryTool',
            img_root='ef_cash_carry_tool',
            images=[
                    ('pick_sheet.png', 'Importing a pick via print to PDF'),
                    ('front_sheet.png', 'Generating a new pdf with extracted details'),
                    ('labels.png', 'Generating pallet labels using extracted information'),
                    ('class_diagram.png', 'Class diagram')
            ]
        )
    ),
    Project(
        name='Rage Request',
        description='Reverse engineered GTA 5’s custom network encryption and created a python library that implemented it to aid in looking for security vulnerabilities for Rockstar Game’s bug bounty program.',
        context='Independent'
    ),
    Project(
        name='Cinema Website',
        description='Worked in a group of four following a scrum methodology to create a fully featured cinema website with booking, admin and analytics functionally written in python using the Flask framework.',
        context='Uni - Year 2 - Software Engineering Project',
        images=ProjectImgs(
            id='cinemaWebsite',
            img_root='cinema_website',
            images=[
                ('home.png', 'Home page'),
                ('login.png', 'Login page'),
                ('browse_movies.png', 'Browse movies page'),
                ('specific_movie.png', 'Movie page'),
                ('seat_selection.png', 'Seat reservation'),
                ('analysis.png', 'Analysis page'),
                ('db_design.png', 'Database design')
            ]
        )
    ),
    Project(
        name='GTA 5 Json Editor',
        description='WinForms tool, written in C#, to edit memory and call in game functions that relate to json objects in Grand Theft Auto 5 on PS3.',
        context='Independent',
        git_link='https://github.com/aaron29th/GTA_5_Json_Editor',
        images=ProjectImgs(
            id='gta5JsonEditor',
            img_root='gta_5_json_editor',
            images=[
                ('objects.png', 'Memory editing dictionaries'),
                ('arrays.png', 'Memory editing arrays'),
                ('misc.png', 'Misc remote procedure call and basic memory editing'),
                ('jobs.png', 'Existing job browser'),
                ('jobs_2.png', 'Job updating and copying menu')
            ]
        )
    ),
    Project(
        name='Web Marketplace',
        description='Developed a responsive marketplace website written in python using the Flask framework.',
        context='Uni - Year 2 - Web application development',
        git_link='https://gitlab.com/AaronRosser/flask_web_marketplace',
        images=ProjectImgs(
            id='webMarketPlace',
            img_root='web_market_place',
            images=[
                    ('user_profile.png', 'User profile'),
                    ('product_listing.png', 'Product listing'),
                    ('manage_account.png', 'Account management'),
                    ('wishlist.png', 'Wishlist'),
                    ('database_model_diagram.png', 'Database deign')
            ]
        )
    ),
    Project(
        name='Qt Video Player',
        description='Worked in a team of six to design and prototype a video player written in C++ using Qt.',
        context='Uni - Year 2 - User Interfaces',
        git_link='https://gitlab.com/AaronRosser/user_interfaces_comp2811_cw3',
        images=ProjectImgs(
            id='qtVideoPlayer',
            img_root='qt_video_player',
            images=[
                    ('player.png', 'Video player'),
                    ('edit_video.png', 'Editing a video\'s details')
            ]
        )
    ),
    Project(
        name='xv6 Operating System Improvements',
        description='Added user mode malloc / free, copy-on-write memory management and implemented a new shell for the xv6 operating system written in C.',
        context='Uni - Year 2 - Operating Systems'
    ),
    Project(
        name='YouTube Notification Bot',
        description='Developed a YouTube Pub/Sub bot written in C# using .Net Core along with a WinForms client application, written in C#, to automatically post tweets and discord messages when YouTube videos were uploaded.',
        context='A Level Computing',
        git_link='https://github.com/aaron29th/ALevelYouTubeNotificationBot'
    ),
    Project(
        name='Argos Tools',
        description='Site to help Argos employees search products without whole cat numbers as well as find similarly pronounced locations to aid with finding missing products.',
        context='Independent',
        git_link='https://github.com/aaron29th/ArgosTools',
        site_link='https://aaronrosser.xyz/argos'
    ),
    Project(
        name='Jack Compiler',
        description='Developed a compiler for the Jack programming language written in C.',
        context='Uni - Year 2 - Compiler Design'
    ),
    Project(
        name='Covid-19 Track and Trace Website',
        description='Developed a website for businesses to record and process customer details for NHS track and trace, written in python using the Flask framework.',
        context='Uni - Year 2 - Software Engineering Principles',
        git_link='https://gitlab.com/AaronRosser/Flask_Covid_Track_Trace',
        images=ProjectImgs(
            id='covidTrackTraceWebsite',
            img_root='covid_track_trace_website',
            images=[
                    ('check_in.png', 'Check in page'),
                    ('editing_business_details.png', 'Mange business page')
            ]
        )
    )
]

if __name__ == "__main__":
    site = Site.make_site(
        outpath="build",
        env_globals={
            'projects': projects
        }
    )
    # enable automatic reloading
    site.render(use_reloader=True)