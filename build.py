from project import Project, ProjectImgs

from staticjinja import Site

projects = [
    Project(
        name='Cinema Website',
        description='Worked in a group of four following a <b>scrum methodology</b> to create a fully featured cinema website with booking, admin and analytics functionally written in <b>python</b> using the <b>Flask framework.</b>',
        context='Uni - Year 2 - Software Engineering Project',
        git_link='https://gitlab.com/comp2913_group_40/software_engineering_project_comp2913',
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
        name='EF Cash Carry Tool',
        description='Developed a proof-of-concept <b>WinForms application</b>, written in <b>C#</b>, to automate regular tasks at work by parsing pdf documents and using the data to generate new pdf documents, this allowed the tasks to be done in less than a quarter of the previous time.',
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
        name='GTA 5 Mission Creator Tool',
        description='<b>WinForms application</b>, written in <b>C#</b>, that makes use of memory editing, remote procedure calling and detours to enable access to an unreleased section of the game.',
        context='Independent',
        git_link='https://github.com/aaron29th/GTA_5_Mission_Creator_Tool',
        images=ProjectImgs(
            id='gta5missionCreator',
            img_root='gta_5_mission_creator',
            images=[
                ('get_json_from_game.png', 'Extracting the created JSON file from the game'),
                ('terminate_script_get_vec3_global.png', 'Changing a Vec3 global variable and terminting an in-game script'),
                ('mission_creator_1.png', 'In-game creator'),
                ('mission_creator_2.png', 'In-game creator'),
                ('mission_creator_3.png', 'In-game creator')
            ]
        )
    ),
    Project(
        name='Rage Request',
        description='Reverse engineered GTA 5\'s custom network encryption and created a <b>python library</b> that implemented it to aid in looking for security vulnerabilities for Rockstar Game’s bug bounty program.',
        context='Independent'
    ),
    Project(
        name='Solar System Simulation',
        description='Desktop <b>Qt</b> application written in <b>C++</b> to demostrate how complex worlds can be created with the <b>legacy fixed function pipeline OpenGL.</b>',
        context='Independent',
        images=ProjectImgs(
            id='solarSystemSimulation',
            img_root='solar_system_simulation',
            images=[
                ('scene_2.png', 'Simulation along with controls and parameter editor'),
                ('diffuse.png', 'Diffusive lighting on Jupiter'),
                ('ufo_orbit.png', 'Hierarchically animated UFO orbiting the sun'),
                ('user_interaction_light_intensity_fov.png', 'Simulation with adjusted FOV and light properties'),
                ('specular_light.png', 'Specular lighting / emission materials on UFO')
            ]
        )
    ),
    Project(
        name='GTA 5 Json Editor',
        description='<b>WinForms application</b>, written in <b>C#</b>, to edit memory and call in game functions that relate to json objects in Grand Theft Auto 5 on PS3.',
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
        description='Developed a responsive marketplace website written in <b>python</b> using the <b>Flask framework.</b>',
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
        description='Worked in a team of six to design and prototype a video player written in <b>C++</b> using <b>Qt.</b>',
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
        description='Added user mode malloc / free, copy-on-write memory management and implemented a new shell for the <b>xv6 operating system</b> written in <b>C.</b>',
        context='Uni - Year 2 - Operating Systems'
    ),
    Project(
        name='YouTube Notification Bot',
        description='Developed a YouTube Pub/Sub bot written in <b>C#</b> using <b>ASP.Net Core</b> along with a <b>WinForms client application</b>, written in <b>C#</b>, to automatically post tweets and discord messages when YouTube videos were uploaded.',
        context='A Level Computing',
        git_link='https://github.com/aaron29th/ALevelYouTubeNotificationBot'
    ),
    Project(
        name='Argos Tools',
        description='Site to help Argos employees search products without whole cat numbers as well as find similarly pronounced locations to aid with finding missing products.',
        context='Independent',
        git_link='https://github.com/aaron29th/ArgosTools',
        site_link='https://aaronrosser.xyz/argos',
        images=ProjectImgs(
            id='argosTools',
            img_root='argos_tools',
            images=[
                ('home.png', 'Home page'),
                ('cat_num_lookup.png', 'Cat num wildcard search'),
                ('check_char_lookup.png', 'Check character lookup'),
                ('check_char_collisions.png', 'Search similar locations with same check character')
            ]
        )
    ),
    Project(
        name='Jack Compiler',
        description='Developed a compiler for the Jack programming language written in <b>C.</b>',
        context='Uni - Year 2 - Compiler Design'
    ),
    Project(
        name='Covid-19 Track and Trace Website',
        description='Developed a website for businesses to record and process customer details for NHS track and trace, written in <b>python</b> using the <b>Flask framework.</b>',
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