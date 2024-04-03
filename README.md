# trial_cdk_python_structure
## 概要
- Pythonコードのディレクトリ構成の例
  - 今回は2案作成した
- CDKはリソース定義を見るために記述した
  - CDKのディレクトリ構成は特にいじってない

## ディレクトリ構成案
1. Branch `01_utils_in_lambda_deploy_package`
   - LambdaのDeploy Packageに全部のhandlerとutilsを入れる
1. Branch `02_utils_in_layer`
   - layerにutilsを入れて、handlerは全て異なるDeploy Packageにする

## ディレクトリ構成詳細
### Branch `01_utils_in_lambda_deploy_package`
```bash
./
├── .flake8
├── .gitignore
├── .npmignore
├── .prettierrc.yml
├── bin/
│  └── trial_cdk_python_structure.ts
├── cdk.json
├── jest.config.js
├── lib/
│  └── trial_cdk_python_structure-stack.ts
├── Makefile
├── package.json
├── pyproject.toml
├── README.md
├── src/
│  ├── __init__.py
│  ├── handlers/
│  │  ├── __init__.py
│  │  └── sample.py
│  └── utils/
│     ├── __init__.py
│     ├── aws/
│     │  ├── __init__.py
│     │  └── aws.py
│     ├── dataclasses/
│     │  ├── __init__.py
│     │  └── load_environments.py
│     └── logger/
│        ├── __init__.py
│        ├── create_logger.py
│        ├── logging_function.py
│        └── logging_handler.py
├── tests/
│  ├── cdk/
│  │  └── trial_cdk_python_structure.test.ts
│  └── unit/
│     ├── conftest.py
│     ├── fixtures/
│     │  └── load_json/
│     │     └── sample.json
│     ├── handlers/
│     │  └── test_sample.py
│     └── utils/
│        └── dataclass/
│           └── test_load_environments.py
└── tsconfig.json
```

### Branch `02_utils_in_layer`
```bash
./
├── .flake8
├── .gitignore
├── .npmignore
├── .prettierrc.yml
├── bin/
│  └── trial_cdk_python_structure.ts
├── cdk.json
├── jest.config.js
├── lib/
│  └── trial_cdk_python_structure-stack.ts
├── Makefile
├── package.json
├── pyproject.toml
├── README.md
├── src/
│  ├── handlers/
│  │  └── sample/
│  │     ├── __init__.py
│  │     └── sample.py
│  └── layers/
│     └── common/
│        ├── __init__.py
│        └── utils/
│           ├── __init__.py
│           ├── aws/
│           │  ├── __init__.py
│           │  └── aws.py
│           ├── dataclasses/
│           │  ├── __init__.py
│           │  └── load_environments.py
│           └── logger/
│              ├── __init__.py
│              ├── create_logger.py
│              ├── logging_function.py
│              └── logging_handler.py
├── tests/
│  ├── cdk/
│  │  └── trial_cdk_python_structure.test.ts
│  └── unit/
│     ├── conftest.py
│     ├── fixtures/
│     │  └── load_json/
│     │     └── sample.json
│     ├── handlers/
│     │  └── test_sample.py
│     └── layers/
│        └── common/
│           └── utils/
│              └── dataclasses/
│                 └── test_load_environments.py
└── tsconfig.json
```
