const { createApp } = Vue

createApp({
    data() {
        return {
            recipes: [],
            //url:'http://localhost:5000/productos', 
            // si el backend esta corriendo local  usar localhost 5000(si no lo subieron a pythonanywhere)
            url: 'https://kimbus2000.pythonanywhere.com/recipes',   // si ya lo subieron a pythonanywhere
            error: false,
            cargando: true,
            /*atributos para el guardar los valores del formulario */
            id: 0,
            nombre: "",
            pelicula: "",
            imagen: "",
            ingredientes: "",
            instrucciones: "",
            descripcion: "",
        }
    },
    computed: {
        ingredientesArray() {
            return this.recipe ? JSON.parse(this.recipe.ingredientes) : [];
        },
        instruccionesArray() {
            return this.recipe ? JSON.parse(this.recipe.instrucciones) : [];
        }
    },
    methods: {
        fetchRecipe(id) {
            fetch(`${this.url}/${id}`)
                .then(response => response.json())
                .then(data => {
                    this.recipe = data;
                    this.cargando = false;
                })
                .catch(err => {
                    console.error(err);
                    this.error = true;
                });
        },
        eliminar(id) {
            const url = this.url + '/' + id;
            var options = {
                method: 'DELETE',
            }
            fetch(url, options)
                .then(res => res.text()) // or res.json()
                .then(res => {
                    alert('Registro Eliminado')
                    location.reload(); // recarga el json luego de eliminado el registro
                })
        },
        
    },
    created() {
        const urlParams = new URLSearchParams(window.location.search);
        const recipeId = urlParams.get('id');
        if (recipeId) {
            this.fetchRecipe(recipeId);
        } else {
            this.error = true;
            this.cargando = false;
        }
    },
}).mount('#app')