sam build --template-file template.yaml --config-file samconfig.toml
sam deploy --template-file template.yaml --config-file samconfig.toml

sam build --template-file template_dev.yaml --config-file samconfig_dev.toml
sam deploy --template-file template_dev.yaml --config-file samconfig_dev.toml