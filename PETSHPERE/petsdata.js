async function fetchallPets() {

  const cachedData = localStorage.getItem("allPets");

  if (cachedData) {

    try {

      const parsedData = JSON.parse(cachedData);

      if (
        Date.now() < parsedData.expiry &&
        parsedData.data.length > 0
      ) {

        console.log("cached");

       
        return parsedData.data;
      }

      localStorage.removeItem("allPets");

    } catch (error) {

      console.error("Error parsing cached pets data:", error);

      localStorage.removeItem("allPets");
    }
  }

  try {
    const response = await fetch(`${API_URL}/petshpere/pets/`);
    const responseData = await response.json();
    if(!response.ok){
      console.log(responseData.error)
      return [];
    }

    localStorage.setItem(
        "allPets",
        JSON.stringify({
          data: responseData,
          expiry: Date.now() + 1000 * 60 * 30
        })
      )
      return responseData.data;
  } catch (error) {
    console.error("Error fetching pets data:", error);
    return [];
  }
}

let allPets = [];
(async()=>{
  allPets = await fetchallPets();
})()




// const petsData = [{
//   id: 1,
//   name: "Golden Retriever",
//   type: "Dog",
//   category: "dog",
//   age: "Adult",
//   gender: "Male",
//   price: 15000,
//   breedInfo: "Golden Retrievers are a popular family breed known for their intelligence, loyalty, and friendly nature. Originally bred as hunting companions, they are highly trainable and excel in obedience, therapy, and service roles.",
//   img: "images/retriever.jpg",
//   images: [
//     "images/retriever1.jpg",
//     "images/retriever2.jpg",
//     "images/retriever3.jpg"
//   ],
//   desc: "A friendly and loyal companion, perfect for families and children.",
//   health: "This pet has received all necessary vaccinations and routine deworming. Regular veterinary check-ups confirm excellent health with no known medical issues.",
//   behavior: "Known for its gentle and affectionate temperament, this dog is highly social and interacts well with children and other pets.",
//   care: "Requires daily exercise, a balanced diet, and regular grooming to maintain coat health and overall well-being.",
//   extra: "Average lifespan: 10–12 years. Highly intelligent and easy to train.",
//   seller: "Kolkata | 9876543210"
// },

// {
//   id: 13,
//   name: "Hamster",
//   type: "Hamster",
//   category: "small",
//   age: "Baby",
//   gender: "Male",
//   price: 800,
//   breedInfo: "Hamsters are small rodents ideal for beginners. They are low-maintenance and suitable for compact living spaces.",
//   img: "images/hamster.jpg",
//   images: [
//     "images/hamster1.jpg",
//     "images/hamster2.jpg"
//   ],
//   desc: "A small and adorable pet, ideal for compact living spaces.",
//   health: "Healthy and active.",
//   behavior: "Nocturnal and playful.",
//   care: "Requires cage and proper food.",
//   extra: "Average lifespan: 2–3 years.",
//   seller: "Kolkata | 9876543210"
// },

// {
//   id: 6,
//   name: "Pomeranian Puppy",
//   type: "Dog",
//   category: "dog",
//   age: "Baby",
//   gender: "Female",
//   price: 6000,
//   breedInfo: "Pomeranians are small companion dogs known for their fluffy coats and lively personalities. They are alert, playful, and ideal for indoor living.",
//   img: "images/pomeranian.jpg",
//   images: [
//     "images/pomeranian1.jpg",
//     "images/pomeranian2.jpg"
//   ],
//   desc: "A small fluffy puppy with a charming personality.",
//   health: "Vaccinated and well cared for.",
//   behavior: "Playful, lively, and affectionate.",
//   care: "Requires grooming and attention.",
//   extra: "Average lifespan: 12–16 years.",
//   seller: "Kolkata | 9876543210"
// },

// {
//   id: 8,
//   name: "Siamese Kitten",
//   type: "Cat",
//   category: "cat",
//   age: "Kitten",
//   gender: "Male",
//   price: 10000,
//   breedInfo: "Siamese cats are known for their striking blue eyes, vocal nature, and strong bond with owners. They are highly social and intelligent.",
//   img: "images/siamese.jpg",
//   images: [
//     "images/siamese1.jpg",
//     "images/siamese2.jpg"
//   ],
//   desc: "An elegant and playful kitten with striking features.",
//   health: "Vaccinated and healthy.",
//   behavior: "Highly social and active.",
//   care: "Needs attention and interaction.",
//   extra: "Average lifespan: 12–15 years.",
//   seller: "Kolkata | 9876543210"
// },

// {
//   id: 15,
//   name: "Parrot",
//   type: "Bird",
//   category: "small",
//   age: "Adult",
//   gender: "Unknown",
//   price: 3500,
//   breedInfo: "Parrots are intelligent birds known for their ability to mimic sounds. They are social and require attention.",
//   img: "images/parrot.jpg",
//   images: [
//     "images/parrot2.jpg",
//     "images/parrot1.jpg"
//   ],
//   desc: "An intelligent bird capable of mimicking sounds and speech.",
//   health: "Healthy and active.",
//   behavior: "Smart and interactive.",
//   care: "Needs stimulation and care.",
//   extra: "Average lifespan: 10–15 years.",
//   seller: "Kolkata | 9876543210"
// },

// {
//   id: 2,
//   name: "Labrador Puppy",
//   type: "Dog",
//   category: "dog",
//   age: "Baby",
//   gender: "Male",
//   price: 9000,
//   breedInfo: "Labradors are one of the most popular dog breeds worldwide. They are known for their friendly personality, intelligence, and adaptability, making them excellent family pets and working dogs.",
//   img: "images/labrador.jpg",
//   images: [
//     "images/labrador1.jpg",
//     "images/labrador2.jpg"
//   ],
//   desc: "A playful and loving puppy, perfect for active families.",
//   health: "Vaccinated as per age and regularly monitored by a veterinarian. Currently healthy and active.",
//   behavior: "Extremely friendly, energetic, and eager to learn.",
//   care: "Needs proper training, high-quality nutrition, and daily playtime.",
//   extra: "Average lifespan: 10–14 years. Highly adaptable.",
//   seller: "Kolkata | 9876543210"
// },

// {
//   id: 7,
//   name: "Persian Cat",
//   type: "Cat",
//   category: "cat",
//   age: "Adult",
//   gender: "Female",
//   price: 12000,
//   breedInfo: "Persian cats are known for their long, luxurious coats and calm temperament. They are one of the most popular indoor cat breeds.",
//   img: "images/persian.jpg",
//   images: [
//     "images/persian1.jpg"
//   ],
//   desc: "A calm and elegant cat with long, beautiful fur.",
//   health: "Fully vaccinated and well maintained.",
//   behavior: "Quiet, relaxed, and affectionate.",
//   care: "Requires daily grooming.",
//   extra: "Average lifespan: 12–15 years.",
//   seller: "Kolkata | 9876543210"
// },

// {
//   id: 16,
//   name: "Lovebird",
//   type: "Bird",
//   category: "small",
//   age: "Young",
//   gender: "Unknown",
//   price: 2000,
//   breedInfo: "Lovebirds are small parrots known for their affectionate nature. They thrive best in pairs.",
//   img: "images/lovebirds.jpg",
//   images: [
//     "images/lovebirds1.jpg",
//     "images/lovebirds2.jpg"
//   ],
//   desc: "A colorful and affectionate bird that thrives in pairs.",
//   health: "Healthy and active.",
//   behavior: "Social and lively.",
//   care: "Needs companionship and care.",
//   extra: "Average lifespan: 8–12 years.",
//   seller: "Kolkata | 9876543210"
// },

// {
//   id: 11,
//   name: "Domestic Shorthair",
//   type: "Cat",
//   category: "cat",
//   age: "Adult",
//   gender: "Female",
//   price: 3000,
//   breedInfo: "Domestic Shorthair cats are mixed-breed cats commonly found in Indian homes. They are adaptable, hardy, and easy to care for.",
//   img: "images/domestic.jpg",
//   images: [
//     "images/domestic1.jpg",
//     "images/domestic2.jpg"
//   ],
//   desc: "A friendly and adaptable cat with a short coat, perfect for Indian homes.",
//   health: "Vaccinated, active, and naturally strong immunity.",
//   behavior: "Playful, independent, and friendly after bonding.",
//   care: "Very low maintenance; minimal grooming required.",
//   extra: "Average lifespan: 12–16 years. Comes in various colors and patterns.",
//   seller: "Kolkata | 9876543210"
// },

// {
//   id: 3,
//   name: "Husky",
//   type: "Dog",
//   category: "dog",
//   age: "Adult",
//   gender: "Female",
//   price: 20000,
//   breedInfo: "Siberian Huskies are working dogs known for their endurance and striking wolf-like appearance. They were originally bred for sled pulling and thrive in active environments.",
//   img: "images/husky.jpg",
//   images: [
//     "images/husky1.jpg"
//   ],
//   desc: "An energetic and intelligent breed known for its striking looks.",
//   health: "Fully vaccinated and maintained under regular veterinary supervision.",
//   behavior: "Highly energetic, intelligent, and independent.",
//   care: "Needs extensive exercise and cooler environments.",
//   extra: "Average lifespan: 12–15 years. Best for active owners.",
//   seller: "Kolkata | 9876543210"
// },

// {
//   id: 4,
//   name: "Beagle Puppy",
//   type: "Dog",
//   category: "dog",
//   age: "Baby",
//   gender: "Male",
//   price: 7000,
//   breedInfo: "Beagles are small to medium-sized hounds known for their strong sense of smell and cheerful personality. They are curious, friendly, and great companions.",
//   img: "images/beagle.jpg",
//   images: [
//     "images/beagle1.jpg"
//   ],
//   desc: "A curious and energetic puppy with a loving nature.",
//   health: "Vaccinated and regularly checked by a veterinarian.",
//   behavior: "Playful, curious, and friendly.",
//   care: "Requires exercise, training, and proper diet.",
//   extra: "Average lifespan: 12–15 years.",
//   seller: "Kolkata | 9876543210"
// },

// {
//   id: 14,
//   name: "Goldfish",
//   type: "Fish",
//   category: "small",
//   age: "Adult",
//   gender: "Unknown",
//   price: 500,
//   breedInfo: "Goldfish are popular freshwater aquarium fish known for their bright color and ease of care.",
//   img: "images/goldfish.jpg",
//   images: [
//     "images/goldfish1.jpg"
//   ],
//   desc: "A beautiful and peaceful aquarium fish.",
//   health: "Healthy and active.",
//   behavior: "Calm and peaceful.",
//   care: "Needs clean water and tank.",
//   extra: "Average lifespan: 5–10 years.",
//   seller: "Kolkata | 9876543210"
// },


// {
//   id: 5,
//   name: "German Shepherd",
//   type: "Dog",
//   category: "dog",
//   age: "Adult",
//   gender: "Male",
//   price: 18000,
//   breedInfo: "German Shepherds are highly intelligent and versatile working dogs. They are widely used in police, military, and security roles due to their loyalty and trainability.",
//   img: "images/shepherd1.jpg",
//   images: [
//     "images/shepherd.jpg"
//   ],
//   desc: "A strong and intelligent breed known for loyalty and protection.",
//   health: "Fully vaccinated and in excellent health condition.",
//   behavior: "Alert, loyal, and protective.",
//   care: "Requires training, exercise, and proper diet.",
//   extra: "Average lifespan: 10–13 years.",
//   seller: "Kolkata | 9876543210"
// },

// {
//   id: 9,
//   name: "Maine Coon",
//   type: "Cat",
//   category: "cat",
//   age: "Adult",
//   gender: "Male",
//   price: 18000,
//   breedInfo: "Maine Coons are one of the largest domestic cat breeds, known for their gentle personality and thick fur. They are often called 'gentle giants'.",
//   img: "images/maine.jpg",
//   images: [
//     "images/maine1.jpg"
//   ],
//   desc: "A large and majestic cat known for its gentle personality.",
//   health: "Vaccinated and well maintained.",
//   behavior: "Calm, friendly, and affectionate.",
//   care: "Requires space and grooming.",
//   extra: "Average lifespan: 12–14 years.",
//   seller: "Kolkata | 9876543210"
// },

// {
//   id: 10,
//   name: "Bengal Kitten",
//   type: "Cat",
//   category: "cat",
//   age: "Kitten",
//   gender: "Female",
//   price: 15000,
//   breedInfo: "Bengal cats are known for their wild appearance and energetic nature. They are highly active and require stimulation.",
//   img: "images/bengal.jpg",
//   images: [
//     "images/bengal1.jpg",
//     "images/bengal2.jpg"
//   ],
//   desc: "A beautiful kitten with a wild appearance and energetic nature.",
//   health: "Vaccinated and healthy.",
//   behavior: "Highly energetic and playful.",
//   care: "Needs space and interaction.",
//   extra: "Average lifespan: 12–16 years.",
//   seller: "Kolkata | 9876543210"
// },

// {
//   id: 12,
//   name: "Rabbit",
//   type: "Rabbit",
//   category: "small",
//   age: "Young",
//   gender: "Female",
//   price: 2500,
//   breedInfo: "Rabbits are gentle small pets known for their calm nature. They are suitable for quiet homes and require gentle handling.",
//   img: "images/rabbit1.jpg",
//   images: [
//     "images/rabbit.jpg",
//     "images/rabbit2.jpg"
//   ],
//   desc: "A soft and gentle pet suitable for quiet homes.",
//   health: "Healthy and active.",
//   behavior: "Calm and friendly.",
//   care: "Needs vegetables and clean space.",
//   extra: "Average lifespan: 5–8 years.",
//   seller: "Kolkata | 9876543210"
// }

// ];