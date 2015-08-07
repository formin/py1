
1.알고리즘 및 코드 설명

 알고리즘 설명: 사용자의 구매 이력 중 감독, 출연자, 장르를 확인하고 관련 컨텐츠의 구매 이력이 많은 상위 컨텐츠 중 해당 사용자에 구매 이력이 없는 컨텐츠 100 개씩을 정리 합니다.  

 main.py: main 실행 파일

  # 영화 컨텐츠정보를 sqlite 에 insert
  module_using_db.iteminfoDB('../oth/item.db','../rsc/round2_itemInfo.tsv')

  # 구매이력정보를 sqlite 에 insert
  module_using_db.purchaseRecordDB('../oth/item.db','../rsc/round2_purchaseRecord.tsv')

  # 구매이력 정보 중 사용자 정보를 정렬
  module_using_db.SortUser('../oth/item.db')

  # 구매이력이 많은 영화 컨텐츠로 정렬
  module_using_db.SortPurchaseRecord('../oth/item.db')

  # 구매이력이 많은 컨텐츠 중 각 사용자가 구매하지 않은 정보를 정렬 후 파일로 저장
  module_using_db.SortData('../oth/item.db','../predict.csv')

 module_using_db.py: 기본 테이블 설명

  # t1 table : 영화 컨텐츠 정보, COL1 컨텐츠, COL2 감독, COL3 출연자, COL4 장르

  # t2 table : 영화 구매 정보 COL1 구매자, COL2 컨텐츠

  # t3 table : 영화 구매이력 많은 순서로 랭킹 COL1 구매자, COL2 컨텐츠

  # t4 table : 전체 사용자 리스트 COL1 구매자

  # t5 table : 사용자가 구매하지 않은 컨텐츠 중 구매 이력이 많은 상위 100 개를 정리 COL1 사용자, COL2 컨텐츠

  # t6 table : 사용자가 구매한 컨텐츠 장르에서 구매하지 않은 컨텐츠 중 구매 이력이 많은 상위 100 개를 정리 COL1 사용자, COL2 컨텐츠 COL4 장르

  # t7 table : 사용자가 구매한 컨텐츠의 출연자에서 구매하지 않은 컨텐츠 중 구매 이력이 많은 상위 100 개를 정리 COL1 사용자, COL2 컨텐츠 COL3 출연자

  # t8 table : 사용자가 구매한 컨텐츠의 감독에서 구매하지 않은 컨텐츠 중 구매 이력이 많은 상위 100 개를 정리 COL1 사용자, COL2 컨텐츠 COL2 감독


2.실행환경 및 실행방법 설명 

 실행환경: python 2.7

 실행방법: python.exe main.py

3.참고문헌

 byte_of_python.pdf
  A Byte of Python
  Swaroop C H <swaroop@swaroopch.com>
  Translated by Jeongbin Park <pjb7687@gmail.com>



