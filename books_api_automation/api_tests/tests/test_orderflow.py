from utils.orchestrator import OrderOrchestrator

def test_order_flow(api_client, headers):
    orchestrator = OrderOrchestrator(api_client, headers)

    book_id = orchestrator.get_book_id()
    order_id = orchestrator.create_order(book_id)

    update_res = orchestrator.update_order(order_id)
    assert update_res.status_code == 204

    delete_res = orchestrator.delete_order(order_id)
    assert delete_res.status_code == 204