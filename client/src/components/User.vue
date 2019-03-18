<template>
  	<tr>
        <td>{{user.name}}</td>
        <td ><a href="#"  v-on:click="$emit('get-user', user.id)">Paid</a></td>
        <td>ipsum</td>
        <td>dolor</td>
        <td>sit</td>
     </tr>
</template>


<script>
	export default {
		name: 'User',
		props : ['user',]
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