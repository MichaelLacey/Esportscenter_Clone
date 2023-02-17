const GET_ONE_GAME = 'get/game'

/* ___________ A C T I O N S   ___________ */
export const getOneGame = (game) => {
    return {
        type: GET_ONE_GAME,
        game
    };
};

/* ___________ T H U N K S   ___________ */
export const getOneGameThunk = (game_id) => async(dispatch) => {
    const response = await fetch(`/api/game/${game_id}`);
    const game = await response.json();
    dispatch(getOneGame(game))
}

/* ___________ R E D U C E R ___________ */
const gameReducer = (state = {}, action) => {
    let newState = {};

    switch(action.type) {
        case GET_ONE_GAME:
            return action.game

        default:
            return state
    };
};

export default gameReducer;