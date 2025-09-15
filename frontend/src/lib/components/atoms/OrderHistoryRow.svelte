<script lang="ts">
	import type { Order } from '$lib/types';
	import { useOrderString } from '$lib/composables/useOrderString';

	interface Props {
		order: Order;
	}

	let { order }: Props = $props();

	const { getOrderString } = useOrderString();
</script>

<div class="grid grid-cols-3 gap-4 p-4 border-b border-slate-100 last:border-b-0 transition-colors">
	<div class="font-semibold text-primary-400">#{order.number}</div>
	<div class="text-primary-500">{getOrderString(order) || 'No items'}</div>
	<div>
		<span
			class={`${order.canceled_at ? 'bg-slate-400' : 'bg-sky-400'} rounded px-2 py-1 text-white text-sm`}
			>{order.canceled_at ? 'Canceled' : 'Pending'}</span
		>
	</div>
</div>
