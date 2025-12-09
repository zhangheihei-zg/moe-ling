const tailwind = require('@tailwindcss/postcss');

module.exports = {
  plugins: [
    tailwind({
      // 可选：指定配置文件路径（默认会自动找）
      config: './tailwind.config.cjs',
    }),
    require('autoprefixer'),
  ],
};
