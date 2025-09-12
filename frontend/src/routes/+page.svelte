<script lang="ts">
	import ItemTotalCard from '$lib/components/atoms/ItemTotalCard.svelte';
	import PlaceOrder from '$lib/components/organisms/PlaceOrder.svelte';
	import OrderHistory from '$lib/components/organisms/OrderHistory.svelte';
	import { ItemType } from '$lib/types';
</script>

<main class="bg-gradient-to-br from-red-50 to-red-100 border-red-200 min-h-screen">
	<div class="container mx-auto px-4 py-8 space-y-8">
		<div class="grid grid-cols-3 gap-12">
			<ItemTotalCard itemType={ItemType.BURGER} />
			<ItemTotalCard itemType={ItemType.FRIES} />
			<ItemTotalCard itemType={ItemType.DRINK} />
		</div>
		<PlaceOrder />
		<OrderHistory />
	</div>
</main>
