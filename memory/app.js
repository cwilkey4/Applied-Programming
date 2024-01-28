document.addEventListener('DOMContentLoaded', () => {
    const grid = document.querySelector('.grid')

    const deck = [
        {
            name: 'blue',
            image: 'images/blue.jpg'
        },
        {
            name: 'blue',
            image: 'images/blue.jpg'
        },
        {
            name: 'green',
            image: 'images/green.jpg'
        },
        {
            name: 'green',
            image: 'images/green.jpg'
        },
        {
            name: 'orange',
            image: 'images/orange.jpg'
        },
        {
            name: 'orange',
            image: 'images/orange.jpg'
        },
        {
            name: 'purple',
            image: 'images/purple.jpg'
        },
        {
            name: 'purple',
            image: 'images/purple.jpg'
        },
        {
            name: 'red',
            image: 'images/red.jpg'
        },
        {
            name: 'red',
            image: 'images/red.jpg'
        },
        {
            name: 'white',
            image: 'images/white.jpg'
        },
        {
            name: 'white',
            image: 'images/white.jpg'
        }
    ]

    let selection = []
    let selectionId = []
    let matched = []

    const selectedCards = deck.sort(() => 0.5 - Math.random())

    function createBoard() {
        for (let i = 0; i < deck.length; i++) {
          const card = document.createElement('img')
          card.setAttribute('src', 'images/star.png')
          card.setAttribute('id', i)
          card.addEventListener('click', flipCard)
          grid.appendChild(card)
        }
      }

    function flipCard() {
        let cardId = this.getAttribute('id')
        if (matched.includes(selection[0]))
        {
            return
        }

        selection.push(deck[cardId].name);
        selectionId.push(cardId);
        this.setAttribute('src', deck[cardId].image);
        if (selection.length ===2) {
          setTimeout(matchCards, 400);
        }
    }

    function matchCards() {
        const cards = document.querySelectorAll('img');
        const firstId = selectionId[0];
        const secondId = selectionId[1];

        // If matched, keep cards flipped over, remove them from unmatched to matched. 
        if (deck[firstId].name === deck[secondId].name)
        {
            cards[firstId].removeEventListener('click', flipCard);
            cards[secondId].removeEventListener('click', flipCard);
            matched.push(selection.slice());

            cards[firstId].style.transform = 'scale(0.85)'; 
            cards[secondId].style.transform = 'scale(0.85)'; 
            cards[firstId].style.opacity = '0.75'; 
            cards[secondId].style.opacity = '0.75'; 
        }
        // If not matched, turn them back over.
        else
        {
            cards[firstId].setAttribute('src', 'images/star.png');
            cards[secondId].setAttribute('src', 'images/star.png');
        }

        selection = []
        selectionId = []

    }

    createBoard()
})