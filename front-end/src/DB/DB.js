
export default class DB {
    constructor() {
        this._animals = [
            { id: 1, shelterId: 2, name: "1назва_тваринки", sex: "дівчинка", type: "пес", age: "1 рік"},
            { id: 2, shelterId: 2, name: "2назва_тваринки", sex: "дівчинка", type: "кіт", age: "2 роки" },
            { id: 3, shelterId: 2, name: "3назва_тваринки", sex: "хлопчик", type: "пес", age: "3 роки" },
            { id: 4, shelterId: 2, name: "4назва_тваринки", sex: "хлопчик", type: "кіт", age: "4 роки" },
            { id: 5, shelterId: 2, name: "5назва_тваринки", sex: "дівчинка", type: "пес", age: "5 років" },
            { id: 6, shelterId: 2, name: "6назва_тваринки", sex: "дівчинка", type: "кіт", age: "6 років" },
            { id: 7, shelterId: 2, name: "7назва_тваринки", sex: "хлопчик", type: "пес", age: "7 років" },
            { id: 8, shelterId: 1, name: "8назва_тваринки", sex: "хлопчик", type: "кіт", age: "8 років" }
        ]

        this._users = [
            { id: 1, name: "Микола" },
            { id: 2, name: "Петро" }
        ]

        this._requests = [
            { id: 1, userId: 1, animalId: 2, status: 0 },
            { id: 2, userId: 1, animalId: 3, status: 2 },
            { id: 3, userId: 2, animalId: 1, status: 2 },
            { id: 4, userId: 2, animalId: 1, status: 2 },
            { id: 5, userId: 2, animalId: 1, status: 2 },
            { id: 6, userId: 2, animalId: 1, status: 2 },
            { id: 7, userId: 2, animalId: 1, status: 2 },
            { id: 8, userId: 2, animalId: 1, status: 2 },
            { id: 9, userId: 2, animalId: 1, status: 2 },
            { id: 10, userId: 2, animalId: 1, status: 2 }

        ]

        this._shelters = [
            { id: 1, name: "shelter1", email: "shelter1@ex.com", phone: "+380111111111", address: "address1", description: "description1" },
            { id: 2, name: "shelter2", email: "shelter2@ex.com", phone: "+380222222222", address: "address2", description: "description2" },
            { id: 3, name: "shelter3", email: "shelter3@ex.com", phone: "+380333333333", address: "address3", description: "description3" }
        ]
    }

    setAnimals(animals) {
        this._animals = animals
    }

    setUsers(users) {
        this._users = users
    }

    setRequests(requests) {
        this._requests = requests
    }

    setShelters(shelters) {
        this._shelters = shelters
    }

    get animals() {
        return this._animals
    }
    get users() {
        return this._users
    }    

    get requests() {
        return this._requests
    }

    get shelters() {
        return this._shelters
    }
    

}