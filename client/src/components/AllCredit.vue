<template>
  	<tr>
        <td>{{credit.name}}</td>
        <td>{{credit.given_date}}</td>
        <td>{{credit.total_amt}}</td>
        <td>{{credit.remaining_current}}</td>
        <td ><a href="#"  v-on:click="$emit('get-user', credit.userdata)">Clear</a></td>     </tr>
</template>


<script>
	export default {
		name: 'AllCredit',
		props : ['credit', 'total']
	}
</script>

<style scoped>
.tuna {
     background:none!important;
     color:lightblue;
     border:none; 
     padding:0!important;
     font: inherit;
     /*border is optional*/
     /* border-bottom:1px solid #444;  */
     cursor: pointer;
}
</style>