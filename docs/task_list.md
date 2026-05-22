# Travel Agent 开发任务清单（v1）

> 目标：一边学习一边开发，按 **P0 → P1 → P2** 小步迭代。  
> 当前状态：已具备 FastAPI 基础接口、请求校验、规则版行程生成。

---

## 0. 当前代码职责（先统一认知）

- `backend/app/main.py`：应用入口与路由装配（不放业务逻辑）
- `backend/app/api/routes/health.py`：健康检查接口
- `backend/app/api/routes/plan.py`：旅行规划 HTTP 接口层
- `backend/app/schemas/plan.py`：请求/响应模型与数据校验
- `backend/app/services/plan_service.py`：行程规划业务编排（后续迁移到 LangGraph）

---

## P0（必须优先完成）— 把“规则函数”升级为“可扩展的 Agent 架构”

### P0-1 输出结构升级（Schema）
- [ ] 在 `PlanResponse` 中新增 `daily_itinerary: List[str]`
- [ ] 新增 `warnings: List[str]`（用于预算不足、日期紧张等提示）
- [ ] 保持现有字段兼容，避免前端立即改动

### P0-2 业务逻辑重构（Service）
- [ ] 将 `generate_plan` 拆分成多个小函数：
  - [ ] `build_summary(...)`
  - [ ] `build_daily_itinerary(...)`
  - [ ] `build_suggestions(...)`
  - [ ] `build_warnings(...)`
- [ ] 加入基础预算判断逻辑（例如人均/天最低预算阈值）
- [ ] 统一返回 `PlanResponse`，减少 route 复杂度

### P0-3 LangGraph 最小接入
- [ ] 新建 `backend/app/agents/travel_graph.py`
- [ ] 定义最小状态 `TravelPlanState`（输入、候选、输出）
- [ ] 先实现 3~4 个节点：
  - [ ] `collect_constraints`
  - [ ] `plan_itinerary`
  - [ ] `validate_plan`
  - [ ] `finalize_response`
- [ ] `plan_service.py` 改为通过 graph 调用（`invoke`）

### P0-4 验证与回归
- [ ] 保证 `POST /api/plan` 入参不变
- [ ] 验证 3 组请求：
  - [ ] 正常样例
  - [ ] 边界样例（days=1、budget=0）
  - [ ] 异常样例（origin=destination）

---

## P1（强烈建议）— 提升可用性与可维护性

### P1-1 增加测试
- [ ] 新建 `tests/test_plan_schema.py`（模型校验测试）
- [ ] 新建 `tests/test_plan_api.py`（接口测试）
- [ ] 增加至少 1 条回归测试覆盖未来 bug

### P1-2 工程能力
- [ ] 增加日志中间件（请求 ID、耗时）
- [ ] 增加统一异常结构（业务错误码、错误信息）
- [ ] 增加配置文件（如 `app/core/config.py`）管理环境变量

### P1-3 响应结构进阶（为前端渲染准备）
- [ ] 把 `daily_itinerary: List[str]` 升级为 `List[DayPlan]`
- [ ] 新增 `budget_breakdown`（交通/住宿/餐饮/门票）
- [ ] 新增 `transport_tips`

---

## P2（产品化）— 接入真实工具与前端闭环

### P2-1 Tool Adapter 抽象
- [ ] 新建 `backend/app/tools/` 目录
- [ ] 实现天气工具适配器（先 mock，再接真实 API）
- [ ] 实现 POI 检索适配器（餐厅/景点）
- [ ] 定义统一工具返回格式，避免供应商锁定

### P2-2 前后端联调
- [ ] 前端表单可提交完整参数（出发地/目的地/日期/预算/偏好）
- [ ] 前端结果页按“天”渲染行程
- [ ] 增加“再生成一次”与“偏好微调”按钮

### P2-3 文档与交付
- [ ] README 增加本地启动与 API 示例
- [ ] README 增加架构图（Route → Service → Graph → Tools）
- [ ] 补充 `docs/` 下迭代记录（每周改了什么）

---

## 每次迭代的固定流程（建议照抄执行）

1. [ ] 先定义/调整 Schema（明确输入输出）
2. [ ] 再改 Service/Graph（实现逻辑）
3. [ ] 最后改 Route（尽量少改）
4. [ ] 写最小测试并本地验证
5. [ ] 更新本文档勾选项与变更说明

---

## 本周建议冲刺（可直接执行）

- Day 1：完成 P0-1
- Day 2：完成 P0-2
- Day 3：完成 P0-3
- Day 4：完成 P0-4 + 修复问题
- Day 5：开始 P1-1（测试）

