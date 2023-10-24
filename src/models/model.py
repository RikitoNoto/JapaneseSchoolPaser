from abc import ABC, abstractmethod
from typing import Any


class Model(ABC):
    def to_dict(self) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for attr in dir(self):
            if not attr.startswith("_"):  # and attr != "to_dict":
                value: Any = eval(f"self.{attr}")
                # 呼び出し可能(関数・メソッド)の場合はスキップ
                if callable(value):
                    continue

                if not isinstance(value, list):
                    result[attr] = value
                    continue

                # リストの場合は各要素にto_dictメソッドを実行
                value_list = []
                for v in value:
                    # Modelを継承している場合はto_dictを実行
                    if isinstance(v, Model):
                        value_list.append(v.to_dict())
                    else:
                        value_list.append(v)
                result[attr] = value_list

        return result
