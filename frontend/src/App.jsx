import { useState } from 'react';
import NovelForm from './components/NovelForm';
import NovelList from './components/NovelList';

function App() {
  const [novels, setNovels] = useState([]);

  const handleNovelCreated = (newNovel) => {
    setNovels(prev => [newNovel, ...prev]);
  };

  return (
    <div className="min-h-screen bg-gradient-to-b from-gray-100 to-gray-200 py-12">
      <div className="container mx-auto px-4">
        <header className="text-center mb-12">
          <h1 className="text-4xl font-bold text-gray-900">墨灵 · AI 小说创作助手</h1>
          <p className="text-gray-600 mt-2">用 AI 激发你的创作灵感</p>
        </header>

        <NovelForm onNovelCreated={handleNovelCreated} />
        <NovelList novels={novels} />
      </div>
    </div>
  );
}

export default App;
