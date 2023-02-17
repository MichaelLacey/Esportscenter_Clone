import './index.css'
import { useHistory, Link } from 'react-router-dom';
import { Redirect } from 'react-router-dom';

export default function Homepage() {
    const history = useHistory();



    return (
        <div className="homepage">
            <div className="trendingTopStories">

                <div className="trending">
                    <div className="title">TRENDING</div>
                    <div className="games">
                        <div id='gamesPtop' onClick={() => history.push('/apexlegends/1')}> <p>APEX LEGENDS</p></div>
                        <div id='borderwidth'></div>
                        <div id='gamesP' onClick={() => history.push('/callofduty/3')}><p>COD: VANGUARD</p></div>
                        <div id='borderwidth'></div>
                        <div id='gamesP' onClick={() => history.push('/valorant/9')}><p>VALORANT</p></div>
                        <div id='borderwidth'></div>
                        <div id='gamesP' onClick={() => history.push('/battlefield/2')}><p>BATTLEFIELD 2042</p></div>
                        <div id='borderwidth'></div>
                        <div id='gamesP' onClick={() => history.push('/halo/6')}><p>HALO INFINITE</p></div>
                        <div id='borderwidth'></div>
                        <div id='gamesPbot' onClick={() => history.push('/gta/5')}><p>GTA V</p></div>
                    </div>
                </div>

                <div className="fallguysdiv">
                    <img src="https://static.wixstatic.com/media/99aa23_9a2376e9af1548d093273d9fa1f318a6~mv2.png/v1/fill/w_526,h_295,fp_0.50_0.50,q_95,enc_auto/99aa23_9a2376e9af1548d093273d9fa1f318a6~mv2.png" alt="" />
                    <div id='fallguyspdiv' ><a className='fallguysATag'>Fall Guys Goes Free to Play</a></div>
                </div>

                <div className="topStories">

                    <div className="title">TOP STORIES</div>

                    <div className="reads">
                        <div className="readDivs"><a className='readsATag' href='https://www.esportscentermedia.com/post/god-of-war-ragnarok-is-coming-this-november'>God of War Ragnarok is Coming This November!!!</a></div>
                        <div id='borderwidth'></div>
                        <div className="readDivs"><a className='readsATag' href='https://www.esportscentermedia.com/post/esports-to-grow-even-more-sony-makes-a-big-investment'>Esports To Grow Even More, Sony Makes a Big Investment</a></div>
                        <div id='borderwidth'></div>
                        <div className="readDivs"><a className='readsATag' href='https://www.esportscentermedia.com/post/multiversus-free-to-play-beta-has-now-released'>Multiversus Free To Play Beta Has Now Released!</a></div>
                        <div id='borderwidth'></div>
                        <div className="readDivs"><a className='readsATag' href='https://www.esportscentermedia.com/post/popular-youtube-streamer-ishowspeed-almost-burns-down-his-house-with-fireworks'>Popular Youtube Streamer, IShowSpeed, Almost Burns Down His House With Fireworks</a></div>
                        <div id='borderwidth'></div>
                        <div className="readDivs"><a className='readsATag' href='https://www.esportscentermedia.com/post/gta-6-rumored-to-have-in-game-crypto-purchases'>GTA 6 Rumored To Have In-game Crypto Purchases?!</a></div>
                    </div>

                </div>

            </div>
            <div className="latestEsports">

                <div className="leftLatestEsports">

                    <div className="followdiv">
                        <p className="followTitle">FOLLOW ESPORTSCENTER</p>
                        <div id='borderwidthLatest'></div>

                        <div className="socialMediadiv">
                            <img src="https://static.wixstatic.com/media/11062b_6e7994bdd94b41178720ff1641a0f323~mv2.png/v1/fill/w_27,h_27,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/11062b_6e7994bdd94b41178720ff1641a0f323~mv2.png" alt="" />
                            <p>TIKTOK</p>
                        </div>
                        <div className="socialMediadiv">
                            <img src="https://static.wixstatic.com/media/9f9c321c774844b793180620472aa4f1.png/v1/fill/w_27,h_27,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/Instagram.png" alt="" />
                            <p>INSTAGRAM</p>
                        </div>
                        <div className="socialMediadiv">
                            <img src="https://static.wixstatic.com/media/44eb1e29ffa34198aee01e8d4f305903.png/v1/fill/w_27,h_27,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/YouTube.png" alt="" />
                            <p>YOUTUBE</p>
                        </div>
                        <div className="socialMediadiv">
                            <img src="https://static.wixstatic.com/media/59687ffffc2042f885062ce2b0744381.png/v1/fill/w_27,h_27,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/Twitter.png" alt="" />
                            <p>TWITTER</p>
                        </div>
                        <div className="socialMediadiv" id='linkedin'>
                            <img src="https://static.wixstatic.com/media/48a2a42b19814efaa824450f23e8a253.png/v1/fill/w_27,h_27,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/LinkedIn.png" alt="" />
                            <p>LINKEDIN</p>
                        </div>
                        <div className="divlinkedin">

                        </div>


                    </div>
                    <div className="popularOrgs">
                        <div className="followTitle">POPULAR ESPORTS ORGS</div>
                        <div id='borderwidthLatest'></div>

                        <div className="sportsOrg">
                            <img src="https://static.wixstatic.com/media/ddb70a_723481355fa44c38a0687d2259f77ded~mv2.png/v1/fill/w_38,h_27,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/faze-logo-social.png" alt="" />
                            <p>FAZE CLAN</p>
                        </div>
                        <div className="sportsOrg">
                            <img src="https://static.wixstatic.com/media/ddb70a_2871cd73a5a64c5991a4c249643d281c~mv2.png/v1/fill/w_27,h_27,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/Black-Logo-Mark.png" alt="" />
                            <p>TSM</p>
                        </div>
                        <div className="sportsOrg">
                            <img src="https://static.wixstatic.com/media/ddb70a_01098d8d90c640c78283fdff2f32b4af~mv2.png/v1/fill/w_40,h_27,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/Logo-Cloud-9_edited.png" alt="" />
                            <p>CLOUD 9</p>
                        </div>
                        <div className="sportsOrg">
                            <img src="https://static.wixstatic.com/media/ddb70a_a145df286789454f92dd6ff4af25cc90~mv2.png/v1/fill/w_27,h_27,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/100_Thieves_logo_svg%20(1).png" alt="" />
                            <p>100 THIEVES</p>
                        </div>
                        <div className="sportsOrg">
                            <img src="https://static.wixstatic.com/media/ddb70a_c6baa5ba3fab4a8c9aa06c4251e1cbce~mv2.png/v1/fill/w_32,h_27,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/1200px-Gen_G_Logo_edited.png" alt="" />
                            <p>GEN G</p>
                        </div>
                        <div className="sportsOrg">
                            <img src="https://static.wixstatic.com/media/ddb70a_01060e8a1be84fe4a8fe38964885d886~mv2.png/v1/fill/w_24,h_28,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/2006132.png" alt="" />
                            <p>G2 ESPORTS</p>
                        </div>
                        <div className="sportsOrg">
                            <img src="https://static.wixstatic.com/media/ddb70a_e021478fcaa64f68886fa56e906126a6~mv2.png/v1/fill/w_38,h_38,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/22ded60518ddaf71975d334849039189cb106e87-1000x1000.png" alt="" />
                            <p>FNATIC</p>
                        </div>
                        <div className="sportsOrg">
                            <img src="https://static.wixstatic.com/media/ddb70a_d6a94e98e0d441138a55ba40c078211d~mv2.png/v1/fill/w_38,h_10,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/NRG_Esports_logo_svg.png" alt="" />
                            <p>NRG</p>
                        </div>

                    </div>

                </div>
                <div className="latestMid">
                    <h4>LATEST</h4>
                    <div id='borderwidthLatestmid'></div>

                    <div className="midNewsLatest">
                        <img src="https://static.wixstatic.com/media/bcb21c_5c26e7881b064fd2b3b29946e317e41a~mv2.png/v1/fill/w_166,h_94,fp_0.50_0.50,q_95,enc_auto/bcb21c_5c26e7881b064fd2b3b29946e317e41a~mv2.png" alt="" />
                        <p>God of War Ragnarok Is Coming This November!!!</p>
                    </div>
                    <div className="midNewsLatest">
                        <img src="https://static.wixstatic.com/media/bcb21c_e2f1917e3cdd427b80cc43066afe95b8~mv2.jpg/v1/fill/w_166,h_94,fp_0.50_0.50,q_90,enc_auto/bcb21c_e2f1917e3cdd427b80cc43066afe95b8~mv2.jpg" alt="" />
                        <p>Esports To Grow Even More, Sony Makes a Big Investment</p>
                    </div>
                    <div className="midNewsLatest">
                        <img src="https://static.wixstatic.com/media/bcb21c_470f7b5dc4e744d2a2b576cff403657d~mv2.png/v1/fill/w_166,h_94,fp_0.50_0.50,q_95,enc_auto/bcb21c_470f7b5dc4e744d2a2b576cff403657d~mv2.png" alt="" />
                        <p>Multiverses Free To Play Beta Has Now Released</p>
                    </div>
                    <div className="midNewsLatest">
                        <img src="https://static.wixstatic.com/media/bcb21c_0a93d84ca4bc4c92978e755a70d1a8df~mv2.png/v1/fill/w_166,h_94,fp_0.50_0.50,q_95,enc_auto/bcb21c_0a93d84ca4bc4c92978e755a70d1a8df~mv2.png" alt="" />
                        <p>Popular Youtube Streamer, IShowSpeed, Almost Burns Down His House With Fireworks</p>
                    </div>
                    <div className="midNewsLatest">
                        <img src="https://static.wixstatic.com/media/bcb21c_5ff7d7e3cbdc4c34abec7dcfb51adfc3~mv2.jpeg/v1/fill/w_166,h_94,fp_0.50_0.50,q_90,enc_auto/bcb21c_5ff7d7e3cbdc4c34abec7dcfb51adfc3~mv2.jpeg" alt="" />
                        <p>GTA 6 Rumored To Have In-game Crypto Purchases?!</p>
                    </div>
                </div>

                <div className="esportsRightDiv">
                    <h4>ESPORTS</h4>
                    <div id='borderwidthLatestmid'></div>

                    <div className="esportsNews">
                        <img src="https://static.wixstatic.com/media/bcb21c_e2f1917e3cdd427b80cc43066afe95b8~mv2.jpg/v1/fill/w_210,h_118,fp_0.50_0.50,q_90,enc_auto/bcb21c_e2f1917e3cdd427b80cc43066afe95b8~mv2.jpg" alt="" />
                        <p>Esports To Grow Even More, Sony Makes a Big Investment</p>
                    </div>
                    <div className="esportsNews">
                        <img src="https://static.wixstatic.com/media/bcb21c_470f7b5dc4e744d2a2b576cff403657d~mv2.png/v1/fill/w_210,h_118,fp_0.50_0.50,q_95,enc_auto/bcb21c_470f7b5dc4e744d2a2b576cff403657d~mv2.png" alt="" />
                        <p>Multiversus Free To Play Beta Has Now Released</p>
                    </div>
                    <div className="esportsNews">
                        <img src="https://static.wixstatic.com/media/bcb21c_2d09904af5f945a2bd21b8cf17441e27~mv2.png/v1/fill/w_210,h_118,fp_0.50_0.50,q_95,enc_auto/bcb21c_2d09904af5f945a2bd21b8cf17441e27~mv2.png" alt="" />
                        <p>XSET Coach Matheus "Budega" Figuiredo Suspended for 12...</p>
                    </div>
                </div>


            </div>

        </div >
    );
};