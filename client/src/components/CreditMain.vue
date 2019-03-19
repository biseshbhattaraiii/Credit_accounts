<template>

  <body>

    
    <div class="container">
      <a href="#" v-on:click="admin_check">Admin</a>
      <div v-if="admin">
      <input type="password" v-model="admin_password" placeholder="Password"/> 
      <button  v-on:click="submitAdmin">Submit</button>
    </div>
      <a href="#" v-on:click="reload">Reload</a>
 
      <div class="row">

        <!-- Blog Entries Column -->
        <div class="col-md-8">

          <h1 class="my-4">Transaction Mananger
          </h1>

          <!-- Blog Post -->
          <div class="card mb-4">
            <div class="card-body">
              <h2 class="card-title">Creditors Book</h2>
                     
      <div class="table-responsive">
        <table class="table table-striped table-sm">
          <thead>
            <tr>
              <th>Name</th>
              <th>Given Date</th>
              <th>Amount</th>
              <th>Remaining</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody v-for="credit in credits" :key="credit.id" >
              <AllCredit v-on:get-user="get_user" v-bind:credit="credit"/>
            
         </tbody>
        </table>
      </div>
                          </div>
            <div class="card-footer text-muted">
             
            </div>
          </div>


            <div v-if = "show" class="card mb-4">
            <div class="card-body">
              <h2 v-if="of_item" class="card-title">{{item_name}}</h2>
              <h2 v-if="of_user" class="card-title">{{this.searchitem}}</h2>
              <h4 class="card-title">No of credits : {{this.no_of_credits}}</h4>
              <h5 v-if="of_user">Total remaining amount : {{remaining_amt_total}}</h5>
              <h5 v-if="of_user">Total paid amt : {{paid_amt_total}}</h5>

              <br>
              <hr>
              <ul v-if="not_paid" class="list-unstyled mb-0" v-for="c in credit_data" :key="c.id">
                <li>Given on : {{c.given_date}}</li>
                <li v-if="of_user">Item : {{c.item_name}}</li>
                <li>Item price : {{c.price}}</li>
                <li>Quantity : {{c.quantity}}</li>
                <li v-if="of_item">Creditor : {{c.name}}</li>
                <!-- <li>Remaining : {{c.remaining}}</li> -->
                <br>
              </ul>

            </div>
          

            </div>
            
        
          
          


      
          <!-- Pagination -->
 
        </div>

        <!-- Sidebar Widgets Column -->
        <div class="col-md-4">

          <!-- Search Widget -->
          <div class="card my-4">
            <h5 class="card-header">Search</h5>
            <div class="card-body">
              <div class="input-group">
               <select v-model="searchitem" class="form-control" id="exampleFormControlSelect1">
                    <option v-for="user in users" :key="user.id">{{user.name}}</option>
               </select>                
                  <span class="input-group-btn">
                  <button v-on:click.prevent="searchUser" class="btn btn-secondary" type="button">Go!</button>
                </span>
              </div>
            </div>
          </div>

          <!-- Categories Widget -->
          <div v-if="no_view" class="card my-4">
            <div class="card-body">
              <div class="row">
                <div class="col-lg-6">
                  <form v-if="paid">
                     <div v-if="never_show" class="form-group">
                          <label for="exampleInputEmail1">Id</label>
                          <input type="number" class="form-control" id="exampleInputEmail1" v-model="user_id">
                        </div>
                        <div class="form-group">
                          <label for="exampleInputEmail1">Total debt</label>
                          <input type="number" class="form-control" id="exampleInputEmail1" v-model="total_amt">
                        </div>
                       
                        <div class="form-group">
                          <label for="exampleInputPassword1">Paid amt</label>
                          <input type="number" class="form-control" v-model="paid_amt" id="exampleInputPassword1" placeholder="Paid amt...">

                          </div>
       
                       
                        <button type="submit" v-on:click.prevent="paidtUser" class="btn btn-primary">Submit</button>
                  </form>
                </div>
               
              </div>
            </div>
            <br>
            
          </div>
          <div  class="card my-4">
            <h5 class="card-header">Add an Item</h5>
            <div class="card-body">
              <div class="row">
                <div class="col-lg-6">
                  <form>
                      <div v-if="add_new_user" class="form-group">
                          <label for="exampleInputPassword1">Name</label>
                          <input type="text" class="form-control" v-model="username" id="exampleInputPassword1" placeholder="Username...">
                          <a href="#" v-on:click="SaveUser">Save</a>
                          </div>
                        <div v-if="add_new_item" class="form-group">
                          <label for="exampleInputPassword1">Item name</label>
                          <input type="text" class="form-control" v-model="itemname" id="exampleInputPassword1" placeholder="Item name...">
                          </div>
                          <div v-if="add_new_item" class="form-group">
                          <label for="exampleInputPassword1">Item price</label>
                          <input type="number" class="form-control" v-model="price" id="exampleInputPassword1" placeholder="Item price...">
                          <a href="#" v-on:click="SaveItem">Save</a>
                          </div>
                     <div class="form-group">
                          <label for="exampleFormControlSelect1">User</label>
                          <select v-model="user" class="form-control" id="exampleFormControlSelect1">
                            <option v-for="user in users" :key="user.id">{{user.name}}</option>
                           
                          </select>
                        </div>
                          <a href="#"  v-on:click="addUser">Add new user</a>
                          <br>
                         <div class="form-group">
                          <label for="exampleFormControlSelect1">Items</label>
                          <select v-model="item" class="form-control" id="exampleFormControlSelect1">
                            <option v-for="item in items" :key="item.id">{{item.item_name}}</option>
                           
                          </select>
                          <a href="#" v-on:click="addItem">Add new item</a>
                          <br>
                        </div>
                        <div class="form-group">
                          <label for="exampleInputEmail1">Quantity</label>
                          <input type="number" class="form-control" id="exampleInputEmail1" v-model="quantity">
                        </div>
                       
                        <div class="form-group">
                          <label for="exampleInputPassword1">Paid amt</label>
                          <input type="number" class="form-control" v-model="paid_amt" id="exampleInputPassword1" placeholder="Paid amt...">

                          </div>
            
                       
                        <button type="submit" v-on:click.prevent="submitCredit" class="btn btn-primary">Submit</button>
                  </form>
                </div>
               
              </div>
            </div>
            <br>
       <!--      <button type="submit" v-on:click.prevent="closeTransaction" class="btn btn-primary">Close transaction</button> -->

          </div>


      
          <!-- Side Widget -->
          <div  class="card my-4">
            <h5 class="card-header">Items</h5>
            <div class="card-body">
            <ul class="list-unstyled mb-0" v-for="item in items" :key="item.id">
              <Credit v-on:get-item-credit="get_item_credit" v-bind:item="item"/>
            </ul>
              <br>
            
           
            </div>
          </div>
        </div>

      </div>
      <!-- /.row -->

    
    </div>
    

  </body>

</template>

<script>
import axios from 'axios';
import Credit from './Credit.vue';
import User from './User.vue';
import AllCredit from './AllCredit.vue'
export default {
  name: 'CreditMain',
  components : {
    User,
    Credit,
    AllCredit
  },
  data () {
    return {
      items : [],
      users : [],
      credits: [],
      searchitem : null,
      show : false,
      no_of_credits : null,
      credit_data : [],
      item_name : null,
      of_item : false,
      of_user: false,
      no_view : false,
      user_id : null,
      never_show : false,
      paid_amt : null,
      total_amt : null,
      total : [],
      not_paid : true,
      add_new_user : false,
      add_new_item : false,
      _new_item_ : true,
      _new_user_ : true,
      username : null,
      itemname : null,
      price : null,
      init_total : [],
      add : true,
      init_total_amt : null,
      paiddata : [],
      remaining_amt_total : null,
      paid_amt_total : null,
      admin : false,
      admin_password : null

    }
  },
  methods : {
    getItems(){
      axios.get('http://127.0.0.1:8000/api/items/')
      .then(response => {
        response.data.forEach(k => {
          this.items.push(k)
        })
      })
    },
    reload(){
      this.$router.go()
    },
    getUser(){
      axios.get('http://127.0.0.1:8000/api/users/')
      .then(response => {
        response.data.forEach(k => {
          this.users.push(k)
        })
      })
    },
    addItem(){
        this.add_new_item = true
        this._new_user_ = false
        this._new_item_ = false
    },
    addUser(){
        this.add_new_user = true
        this._new_item_ = false
        this._new_user_ = false
    },

    paidtUser(){
      this.add = false
      axios.post('http://127.0.0.1:8000/api/paid/', {
        id : this.user_id,
        total_amt : this.total_amt,
        paid_amt : this.paid_amt
      })
      .then(response => console.log(response.data))
      this.$router.go()

   
    },
    submitCredit(){
      if(this.item == null || this.user == null || this.paid_amt == null || this.quantity == null){
        alert("Please fill in the input !")
      }
      axios.post('http://127.0.0.1:8000/api/credit/', {
            item_name : this.item,
            username : this.user,
            paid_amt : this.paid_amt,
            quantity: this.quantity
      })
      .then(response => console.log(response.data))
      this.$router.go()

    },
    get_user(id){
      this.show = false
      this.paid_amt = 0
      this.total_amt = 0
      this.total = []
      this.user_id = id
      this.no_view = true;
      this.paid = true;
      axios.get(`http://127.0.0.1:8000/api/user/remain/${id}/`)
      .then(response => {
        response.data.forEach(k => {
          this.total.push(k.price * k.quantity)
          this.total_amt = k.paid_amt_total + k.remaining_amt_total
          this.paid_amt = k.paid_amt_total
          console.log(k)
          // this.paid_amt = k.paid_amt
        })
         
      })
    },
    admin_check(){
      this.admin = true
    },
    submitAdmin(){
        if (this.admin_password == "linux123"){
          this.admin_password = ''
          window.location.href = 'http://127.0.0.1:8000/admin'
        }else{
          alert("Wrong password")
          this.admin_password = ''
          this.admin = false
        }
    },
    SaveUser(){
      if(this.username == null){
        alert("Please fill in the form !")
      }
      axios.post('http://127.0.0.1:8000/api/users/', {
        name : this.username
      })
      .then(response => console.log(response.data))
      this.$router.go()
    },
    SaveItem(){
      if(this.itemname == null || this.price == null){
        alert("Please fill in the input")
      }
      axios.post('http://127.0.0.1:8000/api/items/', {
        item_name : this.itemname,
        price : this.price
      })
      .then(response => console.log(response.data))
      this.$router.go()
    },
    get_item_credit(id){
      this.total_amt = 0
      this.total = []
      this.no_of_credits = null
      this.of_user = false
      this.show = false;
      this.credit_data = []
      axios.get(`http://127.0.0.1:8000/api/item/${id}/`)
      .then(response => {
        console.log(response.data)
        this.no_of_credits = response.data.length
        response.data.forEach(k => {
          console.log(k)
          this.item_name = k.item_name
          this.credit_data.push(k)
          this.total.push(k)
        })
        
      })
      .catch(err => console.log(err))
      this.of_item = true
      this.show = true
    },
    searchUser(){
      if(this.searchitem == null){
        alert("Please fill in the input !")
      }
      this.total_amt = 0
      this.total = []
      this.no_of_credits = null
      this.of_item = false
      this.show = false
      this.credit_data = []
      this.remaining_amt_total = null
      this.paid_amt_total = null
      axios.get('http://127.0.0.1:8000/api/search/?username='+this.searchitem)
      .then(response => {
        console.log(response.data)
        this.no_of_credits = response.data.length
        if(this.no_of_credits != 0){
          response.data.forEach(k => {
          console.log(k.is_paid)
          this.credit_data.push(k)
          this.paiddata.push(k.paid_amt)
          this.total.push(k.remaining)
          axios.get('http://127.0.0.1:8000/api/user/remain/?username='+this.searchitem)
          .then(response => {
            response.data.forEach(k => {
              console.log(k)
              this.remaining_amt_total = k.remaining_amt_total
              this.paid_amt_total = k.paid_amt_total
            })
          })
        })
        }else{
          // this.of_user = False
        }
        console.log(this.total)
        this.of_user = true
        this.show = true;

      })

    
    },
    getAllCredits(){

      axios.get('http://127.0.0.1:8000/api/credit/')
      .then(response => {
        console.log(response.data)

        response.data.forEach(k => {
          this.credits.push(k)
        })
      })
      .catch(err => console.log(err))

    
    }

  },

  mounted(){
    this.getItems();
    this.getUser();
    this.getAllCredits();

  }
}
</script>

