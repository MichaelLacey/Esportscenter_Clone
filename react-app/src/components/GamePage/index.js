import { useDispatch, useSelector } from "react-redux";
import './index.css';
import { getGameNewsThunk } from "../../store/news";
import { useEffect } from "react";
import { useParams } from 'react-router-dom'
import { getOneGameThunk } from "../../store/games";

export default function GamePage() {
    const dispatch = useDispatch();

    const { gameId } = useParams();

    const game = useSelector(state => state.game)
    const news = Object.values(useSelector(state => state.news));

    console.log('game news', news);
    console.log('game', game)

    useEffect(() => {
        dispatch(getGameNewsThunk(gameId))
        dispatch(getOneGameThunk(gameId))
    }, [gameId]);

    return (
        <div className="gamepageDiv">

            <div className="topDiv">
                <div className="leftDiv">

                    <div className="gameTitle">
                        <h2>{game?.name}</h2>
                    </div>

                    <div className="leftGameNews">
                        <div className="imgandtitle">
                            <img src={news[0]?.image_url} alt="" />
                            <p>{news[0]?.date}</p>
                            <h3>{news[0]?.title}</h3>
                        </div>
                    </div>

                </div>

                <div className="rightDiv">
                    <div className="rightNewstopmid">
                        <div className="titleAndDateRight">
                            <h4>{news[0]?.title}</h4>
                            <p>{news[0]?.date}</p>
                        </div>
                        <img src={news[0]?.image_url} alt="" />
                    </div>
                    <div className="rightNewstopmid">
                        <div className="titleAndDateRight">
                            <h4>{news[1]?.title}</h4>
                            <p>{news[1]?.date}</p>
                        </div>
                        <img src={news[1]?.image_url} alt="" />
                    </div>
                    <div className="rightNewsbot">
                        <div className="titleAndDateRight">
                            <h4>{news[2]?.title}</h4>
                            <p>{news[2]?.date}</p>
                        </div>
                        <img src={news[2]?.image_url} alt="" />
                    </div>

                </div>
            </div>

            <div className="latestDiv">
                <h2>Latest </h2>
                <div className="outerNewsMap">

                    {news && news.map(ele => (
                        <div className="newsMapped">

                            <div className="imgThenTitle">
                                <img src={ele.image_url} alt="" />
                            </div>

                            <div className="rightSideNewsMap">
                                <h4>{ele.title}</h4>
                                <p>{ele.date}</p>
                            </div>

                        </div>
                    ))}
                </div>

            </div>
        </div>

    )
}