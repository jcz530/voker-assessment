import { createQuery, createMutation, useQueryClient } from '@tanstack/svelte-query';
import type { Order } from '$lib/types';

// Hardcoding this for demo purposes
const API_BASE_URL = 'http://127.0.0.1:8000';

async function fetchOrders(): Promise<Order[]> {
	const response = await fetch(`${API_BASE_URL}/orders`);
	if (!response.ok) {
		throw new Error('Failed to fetch orders');
	}
	return response.json();
}

async function submitOrder(message: string): Promise<void> {
	const response = await fetch(`${API_BASE_URL}/orders`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({ message })
	});

	if (!response.ok) {
		const errorData = await response.json();
		throw new Error(errorData.detail || `Failed to submit order: ${response.statusText}`);
	}
}

export function useOrders() {
	return createQuery({
		queryKey: ['orders'],
		queryFn: fetchOrders
	});
}

export function useSubmitOrder() {
	const queryClient = useQueryClient();

	return createMutation({
		mutationFn: submitOrder,
		onSuccess: () => {
			queryClient.invalidateQueries({ queryKey: ['orders'] });
		}
	});
}
