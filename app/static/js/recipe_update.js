console.log(location.search)     // lee los argumentos pasados a este formulario
var id=location.search.substr(4)  // producto_update.html?id=1
console.log(id)
const { createApp } = Vue
  createApp({
    data() {
      return {
        id:0,
        nombre:"",
        pelicula:"",
        descripcion:"",
        ingredientes:"",
        instrucciones:"",
        imagen:"",
        url:'https://kimbus2000.pythonanywhere.com/recipes/'+id,
       }  
    },
    methods: {
        fetchData(url) {
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    console.log(data)
                    this.id=data.id,
                    this.nombre = data.nombre,
                    this.pelicula=data.pelicula,
                    this.descripcion=data.descripcion,
                    this.ingredientes=data.ingredientes,
                    this.instrucciones=data.instrucciones,
                    this.imagen=data.imagen
                })
                .catch(err => {
                    console.error(err);
                    this.error=true              
                })
        },
        modificar() {
            let recipe = {
                nombre:this.nombre,
                pelicula: this.pelicula,
                descripcion: this.descripcion,
                ingredientes: this.ingredientes,
                instrucciones: this.instrucciones,
                imagen: this.imagen
            }
            var options = {
                body: JSON.stringify(recipe),
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                redirect: 'follow'
            }
            fetch(this.url, options)
                .then(function () {
                    alert("Registro modificado")
                    window.location.href = "/recipes"; // navega a productos.html          
                })
                .catch(err => {
                    console.error(err);
                    alert("Error al Modificar")
                })      
        }
    },
    created() {
        this.fetchData(this.url)
    },
  }).mount('#app')
