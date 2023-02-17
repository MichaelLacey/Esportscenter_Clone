import { useHistory } from 'react-router-dom';
import './Navigation.css';

function Navigation() {
	const history = useHistory();

	return (
		<div className='navBigDiv'>

			<div className="innerNavDiv">

				<div className="imgDiv">
					<img src="https://pbs.twimg.com/profile_images/1548122395008872453/IDcm7g3S_400x400.jpg" alt="" />
					<p style={{ color: "rgb(236,240,235)" }} onClick={() => history.push('/')}>Esportscenter</p>
				</div>


				<div className="dropdownsNav"> Games
					<ul className='navDropdownUl'>
						<li onClick={() => history.push('/apexlegends/1')}>Apex Legends</li>
						<li onClick={() => history.push('/battlefield/2')}>Battlefield</li>
						<li onClick={() => history.push('/callofduty/3')}>Call of Duty</li>
						<li onClick={() => history.push('/fortnite/4')}>Fortnite</li>
						<li onClick={() => history.push('/gta/5')}>GTA</li>
						<li onClick={() => history.push('/halo/6')}>Halo</li>
						<li onClick={() => history.push('/rainbow6/7')}>Rainbow 6</li>
						<li onClick={() => history.push('/rocketleague/8')}>Rocket League</li>
						<li onClick={() => history.push('/valorant/9')}>Valorant</li>
					</ul>
				</div>

				<p className='extraNav'>Esports</p>
				<p className='extraNav'>Tech</p>
				<p className='extraNav'>Consoles</p>
				<p className='extraNav'>PC</p>
				<p className='extraNav'>More</p>

			</div>

		</ div>
	);
}

export default Navigation;