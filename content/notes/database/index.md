---
title: 数据库及实现
date: "2025-06-09"
weight: 10
tags: ["Database", "CS", "System", "SQL"]
draft: false
---
{{< katex >}}
## 1 系统概论

- DBS：硬件；软件（应用系统，**DBMS**，OS）；DB；人（用户，管理员）

- DBMS 特点：结构化（数据模型）；共享性高，冗余度低且易扩充；独立性高；统一管控（安全性、完整性、并发控制、恢复）

- DBS 结构：三级模式 **Schema**，二级映像

  子模式（外模式）、**（概念）模式**、内模式；物理独立性与逻辑独立性

- 外部结构：单用户式、分布式和并行、客户机/服务器、浏览器/服务器（SaaS、PaaS、IaaS）

- **数据模型**三要素：数据结构，数据操作，完整性约束

  数据定义语言 **DDL**，数据操纵语言 **DML**（描述式的查询意图）

  （数据抽象）现实世界 - 信息世界 - 计算机世界；概念模型 - 逻辑模型 - 物理模型

- **E-R** 模型：实体、属性、联系，码、域；实体型、实体集、属性型、联系型、度；E-R 图（Chen/Crow）

- 层次（树）、网状（有向图）、关系（二维表：元组/属性；查询效率偏低）、面向对象（维护困难）

  向量、图（知识图谱）；数据仓库

## 2 关系

- 关系模式 $R(U,D,Dom,F)$：元组，属性 $U$、域 $D$、笛卡尔积、关系；（属性向域的映射集 $Dom$）

  超键、候选键（码，能唯一标识元组的最小属性组）、**主键**（主码）、**外键**、代理键（DBMS 分配）；

  **主属性**/非主属性，单码、全码

- 关系运算：\
  集合运算符 $\cap,\ \cup,\ -,\ \times$；逻辑与比较运算符 $\land,\ \vee,\ \neg$；\
  专用运算符 **选择** $\sigma_{\theta}$，**投影** $\Pi$，**连接** $\bowtie_{\theta},\ \bowtie$（一般连接、**自然连接**；内连接、左/右/全外连接 ⟕, ⟖, ⟗、反连接 $\rhd_\theta,\ \rhd$），**除法** $\div$（$R\div S =\{t|t\in \pi_X(R) \wedge t\times\pi_Y(S)\subseteq R\}$，$Y$ 为 $R$ 和 $S$ 相同属性），**重命名** $\rho_{B\leftarrow A}(R),\ \rho_{S}(R),\ \rho_{S(A_1,\dots,A_n)}(R)$

- *例子：S C SC  找出没选过课的学生的姓名；找出选修了所有课程的学生的学号*

- 有序集交集：merge（两个指针，$O(|A|+|B|)$）；二分查找（$O(|A|log|B|)$）；前者两集大小相近更佳（*临界约 32 倍*）

- 数据依赖 $F$（更新异常、冗余），**规范化**（模式分解）

  函数依赖 $X\rightarrow Y$（所有关系实例上的规定），完全函数依赖 $X\overset{f}{\rightarrow}Y$；Armstrong 公理系统

  属性集闭包 $X_F^+ = \{A|A\in U, F\vDash X\rightarrow A\}$，函数依赖集闭包 $F^+$，最小覆盖 $F_C$（分解右部 - 删除左部属性冗余 - 删除函数冗余）

- 范式：**1NF**（属性不可分）、**2NF**（+ 所有非主属性完全依赖每个码）、**3NF**（+ 所有非主属性直接依赖每个码 $Y \nrightarrow X$）、**BCNF**（所有非平凡依赖关系左部为码；*或* 3NF + 所有主属性非平凡*直接完全*依赖每个码）

  *提示*：码 $X,Y \subset U$ 必有 $X\leftrightarrow Y$ 且 $X$ 和 $Y$ 互不包含
  *总结*：检查非主与主之间、主与主之间的完全性与传递性

- **完整性约束**：实体完整性（行不相同、主键不空），参照完整性（外键若不空则取值在参照主键中存在），域完整性（类型格式），用户定义完整性（数据类型和域、缺省和空值、唯一和依赖性）

## 3 设计

- 设计方法：需求分析、概念设计（E-R）、逻辑设计、物理设计、数据库实施、数据库运维

- **需求分析**：业务现状，信息源，外部要求（信息要求、处理要求、安全性与完整性要求）

  业务流程图（用户活动）- 系统范围图 - 数据流图 DFD - 数据字典 DD（数据项、数据结构、数据流、数据存储、处理过程）- 需求说明书

- **概念设计**：局部 E-R 模型 - 全局 E-R 模型 - 优化冗余

  （数据抽象方法）分类（member）、概括（subset）、聚集（part, aspect）；划分局部；定义实体、定义联系（1:1/1:n/m:n）、确定属性（及键）

- **逻辑设计**（特定 MDBS 支持的如关系模型）：实体型关系（多值属性转换为新关系并建立外键约束）；1:1 联系到关系（独立并保留各自的码均可为码，*或*将码和联系属性并入任意一端）；1:n 联系到关系（独立并以 n 端实体的码为码，*或*将 1 端实体的码和联系属性并入 n 端）；m:n 联系到关系（独立并将多元联系的全部实体的码作为码，再加联系的属性）

- **物理设计**：存取方法（索引方法、聚簇方法、HASH 方法），存储结构（顺序存储、散列存储、聚簇存储）

- **行为设计**：功能分析，功能设计，事务设计

- **实施与运维**：数据的载入，应用程序编码和调试，试运行并调试（功能和性能测试）；转储与恢复，安全性、完整性控制，监督与改进，重组（优化存储，不改变物理结构）与重构（涉及模式和内模式的修改）

## 4 MySQL 概述

- MySQL：单进程多线程、支持多用户、基于客户机/服务器的关系数据库管理系统；服务器、实例和数据库，客户程序和工具程序（与服务器通信，多个实例以端口号区分）；服务器语言 SQL

  体系结构 Management Services & Utilities、Connectors、Connection Pool（缓冲连接、线程处理），SQL Interface、Parser、Optimizer、Cache & Buffer，Pluggable Storage Engine、(File System、Files & Logs)

  启动服务 - 配置读入服务器内存 - 生成服务实例进程 - 派生出多个线程 - 客户机与服务器通信链路

- `mysql -u root -p`

- CREATE DROP ALTER RENAME TRUNCATE COMMENT

  SELECT INSERT DELETE UPDATE

  GRANT DENY REVOKE

  SET TRANSACTIION  ROLLBACK COMMIT SAVEPOINT

##  5 库表管理

- 存储引擎（`SHOW ENGINES`；`SHOW VARIABLES LIKE 'storage_engine'`）：\
- **InnoDB**（大数据量、ACID 事务安全、外键，表空间，读写效率低、占用空间大）；\
  **MyISAM**（大量查询，.frm .myd .myi，静态型、动态型、压缩型，空间小速度快）；\
  **MEMORY**（临时表、磁盘只存表结构，HASH 索引，速度快、并发差、浪费内存、重启丢失）；\
  MERGE（一组 MyISAM 表）；BLACKHOLE；CSV；ARCHIVE

  *B-tree、B+tree 索引*

- **字符集**与校对规则（`SHOW CHARACTER SET`；`SHOW VARIABLES LIKE 'character_set_server'`；`SHOW COLLATION WHERE Charset = 'utf8mb4'`）：服务器级、数据库级、表级、字段级（前三者修改只会影响新增数据）；中文，定长；客户端、连接、返回结果的字符集（`SET NAMES ...`）

  *带特殊字符（空格、连字符、点号等）及保留关键字作名称需括反引号*

- 库操作：

  创建 `CREATE {DATABASE|SCHEMA} [IF NOT EXISTS] db_name [[DEFAULT] CHARACTER SET charset_name] [[DEFALUT] COLLATE collation_name]`；

  修改（InnoDB 无法改名）`ALTER {DATABASE|SCHEMA} [db_name] [[DEFAULT] CHARACTER SET [=] charset_name]|[[DEFAULT] COLLATE [=] collation_name]`；

  删除 `DROP DATABASE [IF EXISTS] db_name`；

  切换、查看定义、查看当前 `USE db_name; SHOW CREATE DATABASE db_name; SELECT DATABASE()`；

  `mysqldump -u root -p old_database > backup.sql`，\
  `mysql -u root -p new_database < backup.sql`

- 数值类型 INT(EGER)、SMALLINT、TINYINT、MEDIUMINT、BIGINT，FLOAT、DOUBLE（*精确 10 位以上*）、DECIMAL；\
  日期 YEAR、TIME、DATE、DATATIME、TIMESTAMP；\
  字符串文本 CHAR、VARCHAR、TEXT（不区分大小写，检索效率最低），ENUM（除非约束否则可 NULL）、SET；\
  二进制（仅二进制字符集）BLOB、BIT（位而非字节存储）、BINARY 等

- 表操作：

  创建 `CREATE TABLE [IF NOT EXISTS] 表名 (字段名称 字段类型 [完整性约束条件],...) ENGINE=引擎名称 CHARSET=编码方式`（约束：PRIMARY KEY、FOREIGN KEY、UNIQUE KEY、AUTO_INCREMENT、NOT NULL、DEFAULT、CHECK）；

  查看 `DES[CRIBE] t_name; SHOW CREATE TABLE t_name; SHOW TABLE STATUS [{FROM|IN} db_name] [LIKE 'pattern'|WHERE expr]`；

  **修改** `ALTER TABLE t_name` + `RENAME/TO`，\
  `ADD 字段名称 字段类型 [完整性约束条件] [FIRST|AFTER 字段名称]`、`DROP`、`MODIFY`、`CHANGE`（`旧字段名 新字段名`）、`ALTER 字段名称 SET/DROP DEFAULT`、`ADD [CONSTRAINT symbol] PRIMARY KEY [index_type] (字段名称,...)`、`DROP PRIMARY KEY`，\
  `ADD [CONSTRAINT symbol] UNIQUE [INDEX|KEY] [索引名称] (字段名称,...)`、`DROP {INDEX|KEY} index_name`，`AUTO_INCREMENT=自增长值`；

  复制 `CREATE TABLE T_A LIKE T_B`，`CREATE TABLE T_A AS SELECT ... FROM T_B`（均不复制权限，后者不复制索引）；

  删除 `DROP TABLE [IF EXISTS] t_name[,...]`；\
  `TRUNCATE [TABLE] t_name`（保留表定义）；\
  `DELETE FROM t_name`（DML，保留表定义，不释放空间，可在事务中回滚，速度慢）；

  NULL；IDENTITY\
  *>3 VARCHAR*

- 约束控制（表级、列级）：（子句）`CONSTRAINT 约束名 完整性约束条件`（只用于表级，包括 PRIMARY KEY、FOREIGN KEY、UNIQUE、CHECK，列级的 DEFAULT  NOT NULL 可通过 MODIFY 命名）；更改会校验现有数据

  **主键约束**（UNIQUE + NOT NULL）`PRIMARY KEY (字段名列表)`；\
  **外键约束**（须均使用 InnoDB，非临时表，均有索引，类型相似）`[CONSTRAINT symbol] FOREIGN KEY (本表字段名列表) REFERENCES 父表(父字段名列表) [ON DELETE {CASCADE|SET NULL|RESTRICT|NO ACTION}] [ON UPDATE {CASCADE|SET NULL|RESTRICT|NO ACTION}]`（级联约束）；\
  唯一性约束（允许且不检查 NULL）；非空约束；默认值约束；自增约束（只能于主键/唯一键上）；检查约束

  *MySQL 列级外键约束（仅加 REFERENCES）无效；外键只能使用约束名引用，DROP FOREIGN KEY t_ibfk_1 未删除同名普通索引*

## 6 数据管理

- 插入：`INSERT [INTO] t_name[(字段名称,...)]` + `VALUES|VALUE(值...)`（未赋值字段插入默认值）、`VALUES(值1...),(值2...)...`，`SELECT 字段名称 FROM t_name [WHERE 条件]`（字段数和类型需一致）；`REPLACE [INTO] t_name VALUES(值...)`（唯一约束若已有相同则会覆盖）；

  修改：`UPDATE t_name SET (字段名称＝值,...) [WHERE 条件]`（无 WHERE 将更新全部记录）；

  删除：`DELETE FROM t_name [WHERE 条件]`；

- **查询**：*select_expr* ` 目标列表达式 [AS 别名]`

  *条件* 逻辑 `AND OR XOR NOT`、比较、匹配 `LIKE`（'_'、'%'，`ESCAPE '\'` 转义）`REGEXP 正则表达式`、范围 `BETWEEN 值1 AND 值2; IN 集合`、空值 `IS NULL`

  *分组* 聚合函数（其余列应能聚合）`COUNT ({[ALL|DISTINCT] 字段名}|*)`（不统计 NULL）、`SUM() AVG() MAX() MIN()`

  *NULL 排序时最小*

  ```sql
  SELECT [ALL|DISTINCT] select_expr[,...]
  	[
  		FROM table_references[,...]
  		[WHERE 条件]
  		[GROUP BY 字段名 [ASC|DESC],...]
  		[HAVING 条件2 限制分组结果显示] [WITH ROLLUP]
  		[ORDER BY 字段名 [ASC|DESC],...]
  		[LIMIT {[偏移量,] row_count|row_count OFFSET 偏移量}]
  	]
  ```

  *执行顺序：函数 & 聚合 - SELECT 在 HAVING 之后，ORDER 之前*

- **多表查询**：`表名.列名`，可 `FROM 表名 AS 别名`；连接 `CROSS JOIN`、`[INNER] JOIN`、`NATURAL JOIN`、`LEFT|RIGHT [OUTER] JOIN`；`UNION [ALL]`（列数量和类型一致，会使用第一个语句中的列名）；

  子查询 `[NOT]IN`、`[NOT]EXISTS`、`JOIN`、比较运算符、`ANY()`、`ALL()`；

  查询并插入 `CREATE TABLE|INSERT ... SELECT ...`；

- 传参 `${}` `getRequestString("...")` **SQL注入**（如 `--`）；\
  安全参数 `@var_name` `?` `#{}`，预编译 `PREPARE stmt_name FROM preparable_stmt; EXECUTE stmt_name [USING @var_name [,...]]; DEALLOCATE PREPARE stmt_name`；

## 7 索引

- （键值，地址指针）对；哈希索引（适合等值查询，MyISAM）、有序索引（如 B 树索引）；与主表逻辑独立、物理存储可能分开，降低数据维护速度；\
  **聚簇**/非聚簇索引（一个关系常只有一个聚簇，常为主键，叶子节点常包含完整数据行 InnnoDB、无需回表、减少磁盘 I/O，插入顺序重要，键值更新代价高）

  *书的章节、名词索引*

- **B+ 树**非叶子节点只存储键值，通过叶子链表高效范围查询（聚簇最好）；插入时若溢出（m 阶）则向右分裂并在父节点插入新叶最小键及指针，逐级向上（内节点若需分裂，则左平分指针，右节点多出的键插入其父节点（或新建根节点）及指针）

- 普通索引、唯一性索引 UNIQUE、全文索引 FULLTEXT（字符串）、空间索引 SPATIAL（GEOMETRY、POINT、LINESTRING、POLYGON）；\
  查询条件使用了第一个字段时才会使用索引（B+ 树中应连续存储），条件中不能包含表达式，不能跳过树中的属性；\
  多个单属性索引涉及索引合并，（相比复合索引）效率低

  创建 `CREATE TABLE t_name(..., [UNIQUE|FULLTEXT|SPATIAL] INDEX|KEY [索引名称](字段名称[(长度)] [ASC|DESC]) [USING BTREE|HASH]); CREATE [UNIQUE|FULLTEXT|SPATIAL] INDEX 索引名称 ON t_name (字段名称[(长度)] [ASC|DESC]) [USING BTREE|HASH]; ALTER TABLE t_name ADD [CONSTRAINT symbol] ...`；

  查看 `SHOW INDEX|KEYS FROM t_name [FROM db_name]`（或 `db_name.t_name`）；

  删除 `DROP INDEX index_name ON t_name; ALTER TABLE t_name DROP INDEX index_name`；

- 索引设计：查询与更新分析；**选择度**，**覆盖索引**；调优 REINDEX、ANALYZE

  当条件选择度很高时，聚簇索引 ≈ 非聚簇索引 < 顺序扫描；当条件选择度很低时，聚簇索引 < 顺序扫描 < 非聚簇索引；

  *原则*：限制数目，为常作查询条件的字段、常需连接排序分组联合的字段建立，选择唯一性，使用数据量少或前缀

- **视图**：虚拟表，由查询语句定义（外模式和逻辑独立性、安全性 `GRANT|REVOKE ... ON view_name TO user_name`、灵活性）

  创建 `CREATE [OR REPLACE] [ALGORITHM = {UNDEFINED|MERGE|TEMPTABLE}] VIEW 视图名 [(视图列表)] AS 查询语句 [WITH [CASCADED|LOCAL] CHECK OPTION]`（SELECT 语句不包含子查询、系统或用户变量、预处理参数等，不关联触发程序；WITH CHECK OPTION 保证数据操作满足 WHERE 子句条件）；

  查看、修改，插入、删除、更新数据同表（如 `SHOW CREATE VIEW`、`ALTER ...`、`UPDATE ...`）；可更新视图必须直接映射到基表（如不包含聚合、分组、去重）

  删除 `DROP VIEW [IF EXISTS] view_name[,...] [RESTRICT|CASCADE]`；

## 8 存储过程

- 编译后的一组 SQL 语句

  创建 `CREATE PROCEDURE sp_name ([proc_parameter[,...]]) [characteristic...] [BEGIN] routine_body [END]`（*proc_parameter* `[IN|OUT|INOUT] param_name type`）；

  调用 `CALL sp_name([parameter[,...]])`；

  查看 `SHOW CREATE {PROCEDURE|FUNCTION} sp_name; SELECT * FROM db_name.routines [WHERE routine_name = '名称']`；

  删除 `DROP {PROCEDURE|FUNCTION} [IF EXISTS] sp_name`；

  *DELIMITER 修改语句结束符号*

- 标识符（仅表的别名区分大小写）；常量 b'10'、0b、0x；\
  用户定义会话变量、**局部变量** `DECLARE {local_var type}[,...] [DEFAULT value]; SET @var_name = expr[,...]; SELECT col_name[,...] INTO var_name[,...] FROM t_name [WHERE ...];`（多行只返回最后一行值）`SELECT var_name [AS 'string']`；\
  （系统）**会话变量**、**全局变量** ` SHOW SESSION|GLOBAL VARIABLES; SET SESSION|GLOBAL var_name = value; SET @@session.var_name|@@global.var_name = value;` @@error @@nestlevel

- 表达式（在 SELECT 句使用）：算术运算、位运算、逻辑与比较运算；带 NULL 一般结果为 NULL

- 常用内置**函数**：\
  ASCII() LENGTH() CHAR_LENGTH() CONCAT()（CONCAT_WS()，pipe_as_concat $\vert\vert$）\
  FIELD() FIND_IN_SET() INSERT() LOCATE() POSITION( IN FROM )\
  LOWER() UPPER() SUBSTRING() REPEAT() REVERSE() LPAD/RPAD() LTRIM/RTRIM()（`TRIM([{BOTH|LEADING|TRAILING} [remstr] FROM] str)`）\
  FORMAT() SPACE() LEFT/RIGHT() STRCMP()\
  NOW() DATEDIFF()\
  IF() IFNULL() ISNULL() NULLIF()

  CAST( AS ) CONNECTION_ID() USER() LAST_INSERT_ID()\
  MD5() PASSWORD() ENCODE()

- `CREATE FUNCTION sp_name ([func_parameter[,...]]) RETURNS type [characteristic...] routine_body; SELECT sp_name([func_parameter[,...]])`（*func_parameter* `para_name type`）；

  `SHOW CREATE FUNCTION 函数名; SHOW FUNCTION STATUS [LIKE 'pattern']; DROP FUNCTION 函数名;`

- （异常）**条件处理**：`DECLARE condition_name CONDITION FOR condition_value;`

  `DECLARE [CONTINUE|EXIT|UNDO] HANDLER FOR condition_value[,...] sp_stmt;`

  *condition_value* `{SQLSTATE [VALUE] SQLstate_value|MySQL_error_code|not found|condition_name|SQLwarning|SQLexception}`

- **流程控制**：`IF search_condition THEN stmt_list [ELSEIF search_condition THEN stmt_list] [ELSE search_condition THEN stmt_list] END IF`；\
  `CASE case_value WHEN when_value THEN stmt_list [WHEN when_value THEN stmt_list] [ELSE stmt_list] END CASE`；\
  `[begin_label:] LOOP stm_list END LOOP [end_label]; LEAVE label; ITERATE label`；\
  `[begin_label:] REPEAT stmt_list UNTIL search_confition END REPEAT [end_label]`；\
  `[begin_label:] WHILE search_condition DO stmt_list END WHILE [end_label]`；

- **游标**：`DECLARE cursor_name CURSOR FOR select_stmt; OPEN|CLOSE cursor_name; FETCH cursor_name into var_name[,...];`（SQL Server 需 DEALLOCATE 显式释放游标资源）

## 9 事务

- **触发器**：扩展完整性规则 Event - Condition - Action

  创建 `CREATE TRIGGER trigger_name {BEFORE|AFTER} {INSERT|UPDATE|DELETE} ON t_name FOR EACH ROW trigger_stmt`（永久表上）

  Insert/Delete、NEW/OLD 表

  查看 `SHOW TRIGGERS [FROM db_name]`，或使用 information_schema.triggers 表

  删除 `DROP TRIGGER [IF EXISTS] [db_name.]trigger_name`

  不能调用将数据返回客户端的存储过程，不能采用 CALL 语句的动态 sql，不能使用显式或隐式开始或结束事务的语句；\
  （针对行操作）效率可能低，（MyIsam）不能保证原子性

- **事件**调度器（临时触发器）：定时执行特定任务

  `CREATE EVENT [IF NOT EXISTS] event_name ON SCHEDULE schedule [ON COMPLETION [NOT] PRESERVE] [ENABLE|DISABLE|DISABLE ON SLAVE] [COMMENT 'comment'] DO event_body`

  *schedule* `AT timestamp [+ INTEVEAL quantity]|EVERY quantity [STARTS timestamp] [ENDS timestamp]`

- **权限管理**，user、db、table_priv、columns_priv、procs_priv 表，用户管理

  `GRANT priv_type[(column_list)] [,...] ON [object_type] priv_level TO user[,...] [WITH with_option...]`（转移与次数限制）; \
  `REVOKE priv_type[(column_list)] [,...] ON [object_type] priv_level FROM use r[,...]`（`REVOKE all privileges，grant option FROM user` 回收全部权限）

- 原子性、一致性、隔离性、持久性；调度，异常（脏写、脏读、不可重复读、幻读）；\
  **隔离级别** `SET [SESSION|GLOBAL] TRANSACTION ISOLATION LEVEL {READ UNCOMMITTED|READ COMMITTED|REPEATABLE READ|SERIALIZABLE}`

  START TRANSACTION; COMMIT; ROLLBACK;

- 交叉/同时并发；**锁**机制（表级、页面级、行级（InnoDB，加锁慢、易死锁，并发度高）），共享锁/互斥锁；\
  **死锁**，超时/等待图检测，牺牲品；约定顺序，尽量排他

## 10 查询执行

- **LSM 树**：异地更新，空间放大高，顺序I/O（高性能写），并发控制与故障恢复简单

  SQL Parser & Translator - (relational algebra expression) - Query Optimizer - (physical query execution plan) - Query Executor

- （对索引项）排序执行算法：外排序，两趟**多路归并**（创建若干个归并段，各含若干页；每页含 $B$ 个元组，共 $B(R) = \lceil \frac{T(R)}{B}\rceil$ 页/块；内存要求 $B(R)\le M^2$；I/O 代价 $3B(R)$），多趟多路（$(2m-1)B(R)$；双缓冲优化）

  选择执行算法（内存要求 $M\ge 1$）：一趟扫描（聚簇 $B(R)$ 或非聚簇 $T(R)$）、哈希（访问桶的页面链 $\approx \lceil \frac{B(R)}{V(R,K)}\rceil$）、索引（$\approx \lceil \frac{B(R)}{V(R,K)}\rceil$ 或 $\lceil \frac{T(R)}{V(R,K)}\rceil$）

  投影执行算法（$M\ge 1$，I/O $B(R)$ 或 $T(R)$）

  去重执行算法：一趟（$B(\delta(R))\le M-1$，I/O $B(R)$ 或 $T(R)$）、排序（多路归并时仅输出不同的）、 哈希（$B(R)\le (M-1)^2$，I/O 分桶读 + 写 + 逐桶去重 $3B(R)$）；聚集类似

  集合差执行算法：一趟（build + probe，$B(S)\le M-1$，I/O $B(R)+B(S)$）、哈希（$B(S)\le (M-1)^2$，I/O $3B(R)+3B(S)$）、排序（同理 3）；并、交类似

  连接执行算法：一趟（build + probe 同上）、嵌套循环（outer + inner，$M\ge 2$，I/O 基于行 $T(S)(T(R)+1)$ 或基于块 $B(S)+\frac{B(R)B(S)}{M-1}$）、排序（按连接属性排，$B(R)+B(S)\le M^2$，I/O $3B(R)+3B(S)$）、哈希（两桶间一趟，要求和代价同上）、索引（$M\ge 2$，$B(R)+T(R)\lceil \frac{B(S)}{V(S,Y)}\rceil$ 或 $B(R)+\frac{T(R)T(S)}{V(S,Y)}$）

  物化执行、流水线执行/火山模型

- 逻辑/物理**查询优化**（NP-hard）：选择下推（选择度、预先分解、有无索引），投影下推，枚举代价（以中间结果基数估计I/O次数）；\
  ANALYZE 统计信息（$T(R), V(R,A)$），基数估计时假设各属性均匀分布、互相独立；\
  **左深连接树**（树数量少、缓冲需求低、不多次物化中间关系）

  $T(\sigma_{A=a}(R)) = \frac{T(R)}{V(R,A)},\ T(R\bowtie S) = \frac{T(R)T(S)}{\prod_i \max \{V(R,X_i), V(S,X_i)\}}$

  索引扫描 + 过滤、多索引扫描 + 求交集、仅用索引、顺序扫描

  *流水线例子：哈希分桶、逐桶连接（3B(R)+3B(S)+B(U) 或缓冲区不足 3B(R)+3B(S)+2B(R join S)+3B(U)，2来自于无需读取原始数据，已按哈希预分）*

## 11 其他

- **分布式 DDB**：分层模式结构（全局外模式、全局概念模式、分片模式、**分布模式**、局部概念模式、局部内模式）；分片和位置透明性；数据分片与分配分离、冗余显式控制、局部 DBMS 独立性

- 数据复制（更新传播问题）、**数据分片**；分片条件：完备性、不相交（垂直分片除外）、可重构

- **NoSQL**：各数据独立设计、易分散；数据模型灵活、可扩展性、高性能，维护简单，分布式计算；没有声明性查询语言、没有预定义模式、没有非结构化和不可预知的数据

  关系数据库劣势：大量写入、更新表索引和结构、字段不固定时应用存在困难，简单查询响应慢

  临时性键值存储（内存中，MemCached、Redis）、永久性键值存储（ROMA、Redis）、面向文档（不定义表结构、可利用复杂的查询条件，MongoDB、CouchDB）、面向列（Cassandra、HBase）、图（RDF 三元组）、向量

- **CAP** 理论：（不可能同时很好的满足）一致性、可用性、分区容错性

  CA 单点集群 RDMBS，CP MongoDB、Redis，AP CouchDB、Cassandra