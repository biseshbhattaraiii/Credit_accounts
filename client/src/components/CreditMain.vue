<template>
  <div class="col-md-8">

          <h1 class="my-4">Credit accounts</h1>

          <!-- Blog Post -->
          <div class="card mb-4">
            <div class="card-body">
              <h2 class="card-title">Items</h2>
                      <ul class="list-unstyled mb-0"  v-for="item in items" :key="item.id" >
                        <Credit/>
                      </ul>
              <h2></h2>
            </div>
              <div class="card-body">
              <h2 class="card-title">Users</h2>
                      <ul class="list-unstyled mb-0"  v-for="user in users" :key="user.id" >
                        <User/>
                      </ul>
            
            </div>
</div>
</div>

</template>

<script>
import axios from 'axios';
export default {
  name: 'CreditMain',
  components : {
    User,
    Credit
  },
  data () {
    return {
      items : [],
      users : []
    }
  },
  methods : {
    getItems(){
      axios.get('http://127.0.0.1:8000/api/items/')
      .then(response => {
        this.items.push(response.data)
      })
    },
    getUser(){
      axios.get('http://127.0.0.1:8000/api/users/')
      .then(response => {
        this.users.push(response.data)
      })
    },
    paid(id){
      axios.get('http://127.0.0.1:8000/api/paid'+id)
      .then(response => {
        console.log(response.data)
        this.$router.go()
      })
    }
  },
  mounted(){
    this.getItems();
    this.getUser();
  }
}
</script>

