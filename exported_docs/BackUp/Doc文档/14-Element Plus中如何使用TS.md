# Element Plus中如何使用TS
## Element Plus中使用TS
Element Plus默认就是高度集成TS的支持，不过为了更好的能让Element Plus进行提示效果，还是需要做一些处理配置的。

如果您使用 Volar，请在 tsconfig.json 中通过 compilerOptions.types 指定全局组件类型"types": ["element-plus/global"]

```json
// tsconfig.json
"types": [
    "webpack-env",
    "element-plus/global"
]
```

配置好后，当输入<的时候，就会自动带有提示组件功能，以及组件属性与属性值的提示效果。

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2023/png/21382055/1684562319161-60fbcb96-3c91-42f5-93fb-fa2ed620856f.png)

ElmentPlus组件名提示

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2023/png/21382055/1684562319258-c08ccab6-3e8c-47b4-ab0b-2b5925e4d2cd.png)

ElmentPlus组件属性提示

这里需要注意，由于Volar插件更新比较快，如果不能很好进行提示的话，可以把Volar插件降级到1.0.0这个版本。

除了提示外，Element Plus默认带有的类型都可以在Vue项目中引入，并进行使用，例如表单控件，代码如下：

```vue
<script lang="ts" setup>
import { reactive, ref } from 'vue'
import type { FormInstance, FormRules } from 'element-plus'
const ruleFormRef = ref<FormInstance>()
const rules = reactive<FormRules>({
})
const submitForm = async (formEl: FormInstance | undefined) => {
}
```

FormInstance用于定义表单实例的类型，FormRules用于定义表单规则的类型等。

