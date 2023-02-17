const GET_GAME_NEWS = 'get/game/news'




/* ___________ A C T I O N S   ___________ */
export const getGameNewsAction = (news) => {
    return{
        type:GET_GAME_NEWS,
        news
    };
};

/* ___________ T H U N K S   ___________ */
export const getGameNewsThunk = (game_id) => async(dispatch) => {
    const response = await fetch(`/api/news/${game_id}`);
    const news = await response.json();
    console.log('news for game ', news.News)
    dispatch(getGameNewsAction(news.News));
}

/* ___________ R E D U C E R ___________ */
const newsReducer = (state = {}, action ) => {
    let newState = {};

    switch(action.type) {

        case GET_GAME_NEWS:
            // action.news.forEach(news => newState[news.id] = news)
            return action.news

        default: 
            return state
    };
};

export default newsReducer;