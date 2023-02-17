import './index.css'
import { useHistory } from 'react-router-dom';

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
                    <div id='fallguyspdiv'><p>Fall Guys Goes Free to Play</p></div>
                </div>

                <div className="topStories">

                    <div className="title">TOP STORIES</div>

                    <div className="reads">
                        <div className="readDivs"><p>God of War Ragnarok is Coming This November!!!</p></div>
                        <div id='borderwidth'></div>
                        <div className="readDivs"><p>Esports To Grow Even More, Sony Makes a Big Investment</p></div>
                        <div id='borderwidth'></div>
                        <div className="readDivs"><p>Multiversus Free To Play Beta Has Now Released!</p></div>
                        <div id='borderwidth'></div>
                        <div className="readDivs"><p>Popular Youtube Streamer, IShowSpeed, Almost Burns Down His House With Fireworks</p></div>
                        <div id='borderwidth'></div>
                        <div className="readDivs"><p>GTA 6 Rumored To Have In-game Crypto Purchases?!</p></div>
                    </div>

                </div>

            </div>
            <div className="latestEsports">

                {/* <div className="followdiv">
                    <div className="followTitle">FOLLOW ESPORTSCENTER</div>
                    <div id='borderwidthLatest'></div>
                </div> */}
            </div>

        </div >
    );
};