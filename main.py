# noinspection SpellCheckingInspection
__author__ = 'wookjae.jo'

from datetime import datetime

import fetcher


def main():
    print('모든 티커 정보 조회:')
    print(fetcher.tickers())
    print('=' * 100)

    print('모든 티커 이름 조회:')
    print(fetcher.ticker_names())
    print('=' * 100)

    print('Ohlcv per a minute:')
    for x in fetcher.fetch_ohlcv(
            symbol='ETH/BTC',
            time_frame=fetcher.TimeFrame(fetcher.TimeUnit.MINUTE, 1),
            begin=datetime(2021, 5, 1),
            end=datetime.now()):
        print(x)

    print('=' * 100)

    print('Ohlcv per a minute as list:')
    # 여러 번의 API 호출 후 결과를 병합하여 반환하기 때문에 다소 시간 소요됩니다.
    # 오랜 기간에 대해 아래와 같은 방법으로 데이터를 받아오는 과정에서 메모리 터질 수 있음에 주의 바랍니다.
    result = list(fetcher.fetch_ohlcv(
        symbol='ETH/BTC',
        time_frame=fetcher.TimeFrame(fetcher.TimeUnit.MINUTE, 1),
        begin=datetime(2021, 5, 1),
        end=datetime.now())
    )
    print(result)
    print('=' * 100)

    print('Ohlcv per a day:')
    result = list(fetcher.fetch_ohlcv(
        symbol='ETH/BTC',
        time_frame=fetcher.TimeFrame(fetcher.TimeUnit.DAY, 1),
        begin=datetime(2021, 5, 1),
        end=datetime.now())
    )
    print(result)


if __name__ == '__main__':
    main()
