# 架构与内容模型

这是以 Markdown 为正文、YAML 为导航索引的轻量知识库。

- `registry/projects.yaml`：项目元数据和专题 ID；单个项目稳定 ID。
- `registry/topics.yaml`：技术专题及其说明文件；专题可跨多个项目。
- `registry/relationships.yaml`：具备证据的上下游/衍生关系；避免推断。
- `projects/*.md`：项目来源、功能、限制与可信等级。
- `topics/*.md`：从问题出发汇总多个项目，避免复制其全部文档。

项目和专题之间是多对多关系。项目归属、技术专题、证据等级是三条独立轴线。后续如果增加 RAG，必须保留引用来源、版本元数据和审查制度。
