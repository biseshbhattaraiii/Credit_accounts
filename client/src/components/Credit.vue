<template>
	<li><a class="tuna" href="#" v-on:click="$emit('get-item-credit', item.id)">{{item.item_name}}</a></li>
</template>

<script>
	export default {
		name: "Credit",
		props : ['item',],
		data (){
			return {


			}
		}
	}
</script>

<style scoped>
.tuna {
     background:none!important;
     color:darkblue;
     border:none; 
     padding:0!important;
     font: inherit;
     /*border is optional*/
     /* border-bottom:1px solid #444;  */
     cursor: pointer;
}
</style>