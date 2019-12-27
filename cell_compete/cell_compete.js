function cell(states, days) {

  // operate for each day
  for (let i = 0; i < days; i++) {
    states = determineNextCellStates(states)
  }

  return states
}

function determineNextCellStates(states) {

  // first and last cells get the value of their neighbors
  let newStates = [cells[1], 0, 0, 0, 0, 0, 0, cells[6]]

  for (let i = 1; i < cells.length - 1; i++) {

    // if both neighbors are the same value, deactivate
    if (cells[i - 1] === cells[i + 1]) {
      newStates[i] = 0
    } else {
      newStates[i] = 1
    }
  }

  return newStates
}

module.exports = cell