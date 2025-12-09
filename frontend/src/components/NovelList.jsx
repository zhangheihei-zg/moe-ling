export default function NovelList({ novels }) {
  if (novels.length === 0) {
    return (
      <div className="text-center py-8 text-gray-500">
        还没有创作任何小说，快去写一篇吧！
      </div>
    );
  }

  return (
    <div className="max-w-2xl mx-auto mt-8">
      <h2 className="text-xl font-bold mb-4 text-gray-800">我的小说</h2>
      <div className="space-y-4">
        {novels.map((novel) => (
          <div key={novel.id} className="p-4 border border-gray-200 rounded-lg bg-gray-50">
            <div className="font-bold text-lg text-blue-700">#{novel.id} {novel.title}</div>
            <div className="mt-2 text-gray-700 line-clamp-3">{novel.content}</div>
          </div>
        ))}
      </div>
    </div>
  );
}
