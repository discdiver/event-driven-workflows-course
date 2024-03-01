from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from prefect.events import emit_event


def get_quote(ticker: str) -> float:
    """Fetch a stock quote from the web"""
    print("fetching data")
    share_price = 200.03
    emit_event(
        event="airflow.dag.get_quote.running",
        resource={
            "prefect.resource.id": "airflow.dag.quote",
            "name": "Fetch stock quote",
            "share_price": share_price,
            "ticker": ticker,
        },
    )
    return share_price


def write_data(ticker: str, price: float) -> None:
    """Write data"""
    print("writing data")
    return


def main() -> None:
    """Main dag assembly function"""
    ticker = "AAPL"
    price = get_quote(ticker=ticker)
    write_data(ticker, price)
    return


with DAG(
    dag_id="get_stock_quote",
    start_date=datetime(2023, 12, 12),
    schedule="@hourly",
    catchup=False,
) as dag:
    task1 = PythonOperator(task_id="example_task", python_callable=main)
