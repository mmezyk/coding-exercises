'use strict';

// Selecting DOM elements
const score0 = document.querySelector('#score--0');
const score1 = document.querySelector('#score--1');
const current0 = document.querySelector('#current--0');
const current1 = document.querySelector('#current--1');
const dice = document.querySelector('.dice');
const player0 = document.querySelector('.player--0');
const player1 = document.querySelector('.player--1');
let currentScore, scores, keepPlaying;

// Checking which player is active
function activePlayer() {
  if (
    document.querySelector('.player--0').classList.contains('player--active')
  ) {
    return 0;
  } else {
    return 1;
  }
}

// Changing the player
function playerChange() {
  player0.classList.toggle('player--active');
  player1.classList.toggle('player--active');
}

// Setting the initial conditions
function init() {
  keepPlaying = true;
  score0.textContent = 0;
  score1.textContent = 0;
  current0.textContent = 0;
  current1.textContent = 0;
  dice.style.display = 'none';
  currentScore = 0;
  scores = [0, 0];
  activePlayer() === 1 ? playerChange() : {};
  if (player0.classList.contains('player--winner')) {
    player0.classList.remove('player--winner');
  } else if (player1.classList.contains('player--winner')) {
    player1.classList.remove('player--winner');
  }
}

// Updating the total score
function updateScore(currentScore, scores) {
  const playerId = activePlayer();
  scores[playerId] += currentScore;
  document.querySelector(`#score--${playerId}`).textContent = scores[playerId];
  document.querySelector(`#current--${playerId}`).textContent = 0;
  if (scores[playerId] >= 100) {
    document
      .querySelector(`.player--${playerId}`)
      .classList.add('player--winner');
    dice.style.display = 'none';
    return false;
  } else {
    return true;
  }
}

// Updating the current score
function updateCurrentScore(currentScore) {
  const playerId = activePlayer();
  document.querySelector(`#current--${playerId}`).textContent = currentScore;
}
// Showing the dice image
function showDice(number) {
  dice.style.display = '';
  dice.src = `dice-${number}.png`;
}

init();

// Rolling the dice
document.querySelector('.btn--roll').addEventListener('click', function () {
  let number = Math.trunc(Math.random() * 6) + 1;
  showDice(number);
  if (number !== 1 && keepPlaying) {
    currentScore += number;
    updateCurrentScore(currentScore);
  } else if (number === 1 && keepPlaying) {
    currentScore = 0;
    updateCurrentScore(currentScore);
    playerChange();
  } else {
    currentScore = 0;
    updateCurrentScore(currentScore);
    dice.style.display = 'none';
  }
});
// Saving the current score
document.querySelector('.btn--hold').addEventListener('click', function () {
  keepPlaying = updateScore(currentScore, scores);
  if (keepPlaying) {
    currentScore = 0;
    scores[0] = Number(score0.textContent);
    scores[1] = Number(score1.textContent);
    playerChange();
    dice.style.display = 'none';
  }
});

// Resetting the game
document.querySelector('.btn--new').addEventListener('click', init);
