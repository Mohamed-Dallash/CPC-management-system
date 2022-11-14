export default class APIService{
    static async loginUser(email){
        try {
            const response = await fetch(`http://127.0.0.1:5000/login`, {
                'method': 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(email)
            })
            response.json()
                .then(function (data) {
                })
        } catch (error) {
            return console.log(error)
        }
    }

}