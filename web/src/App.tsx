import { useState, useEffect } from 'react';
import * as Dialog from '@radix-ui/react-dialog';
import { CreateAdBanner } from './assets/components/CreateAdBanner';
import { GameController } from 'phosphor-react';
import { GameBanner } from './assets/components/GameBanner';

import './styles/main.css';

import logoImg from './assets/logo-nlw-esports.svg';
import { Input } from './assets/components/Form/Input';


interface Game {
  id: string;
  title: string;
  bannerUrl: string;
  _count: {
    ads: number;
  }
}

function App() {
  const[games, setGames] = useState<Game[]>([])

  useEffect(() => {
    fetch('http://localhost:4444/games')
    .then(response => response.json())
    .then(data => {
      setGames(data)
    })
  }, [])



  return (
    <div className="max-w-[1344px] mx-auto flex flex-col items-center my-20">
      <img src={logoImg} alt="" />
      <h1 className="text-6xl text-white font-black mt-20">
        Seu <span className="text-transparent bg-nlw-gradient bg-clip-text"> duo </span> está aqui.
        </h1>
        <div className="grid grid-cols-6 gap-6 mt-16">

          {games.map(game => {
            return (
              <GameBanner
              key={game.id}
              title={game.title} 
              bannerUrl={game.bannerUrl}
              adsCount={game._count.ads} />
            )
          })}

        </div>
        
        <Dialog.Root>
          <CreateAdBanner />
          <Dialog.Portal>
            <Dialog.Overlay className='bg-black/60 inset-0 fixed' />
            <Dialog.Content className='fixed bg-[#2A2634] py-8 px-10 text-white top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 rounded-lg w-[480px] shadow-lg shadow-black/25'>
              <Dialog.Title className='text-3xl font-black'>Publique um anúncio</Dialog.Title>
              <form className="mt-8 flex flex-col gap-4">
                  <div className="flex flex-col gap-2">
                    <label htmlFor="game" className="font-semibold"> Qual o game? </label>
                    <Input placeholder="Selecione o game que deseja jogar"
                    id="game" />
                  </div>
                  <div className="flex flex-col gap-2">
                    <label htmlFor="name"> Seu nome ou Nickname</label>
                    <Input 
                    type="text" 
                    placeholder="Como te chamam dentro do game?" 
                    id="name" />
                  </div>
                  
                  <div className="grid grid-cols-2 gap-6">
                    <div className="flex flex-col gap-2">
                      <label htmlFor="yearsPlaying"> Joga a quantos anos? </label>
                      <Input 
                      type="number" 
                      placeholder="Tudo bem ser ZERO" 
                      id="YearsPlaying" />
                    </div>
                    <div className="flex flex-col gap-2">
                      <label htmlFor="discord"> Qual seu Discord? </label>
                      <Input 
                      type="text" 
                      placeholder="usuario#0000" 
                      id="discord" />
                    </div>

                    <div className="flex flex-col gap-4">
                      <div className="flex flex-col gap-2">
                        <label htmlFor="weekDays"> Quando costuma jogar?</label>
                        <div className="grid grid-cols-7 gap-14">
                          <button 
                          title="Domingo"
                          className="w-8 h-8 rounded bg-zinc-900"
                          >D</button>
                          <button 
                          title="Segunda"
                          className="w-8 h-8 rounded bg-zinc-900"
                          >S</button>
                          <button 
                          title="Terça"
                          className="w-8 h-8 rounded bg-zinc-900"
                          >T</button>
                          <button 
                          title="Quarta"
                          className="w-8 h-8 rounded bg-zinc-900"
                          >Q</button>
                          <button 
                          title="Quinta"
                          className="w-8 h-8 rounded bg-zinc-900"
                          >Q</button>
                          <button 
                          title="Sexta"
                          className="w-8 h-8 rounded bg-zinc-900"
                          >S</button>
                          <button 
                          title="Sabado"
                          className="w-8 h-8 rounded bg-zinc-900"
                          >S</button>
                        </div>

                      </div>
                      <div className="flex flex-col gap-2">
                        <label htmlFor="hourStart">Qual horario do dia?</label>
                        <div className="grid grid-cols-2 gap-2">
                          <Input type="time" placeholder="De" id="hourStart" />
                          <Input type="time" placeholder="Até" id="hourEnd" />
                        </div>
                      </div>
                    </div>
                    <div className="mt-14 flex items-center gap-2 text-sm">
                      <Input
                      type="checkbox"
                      className="w-4 h-4 text-emerald-400"
                      />
                      Costuma se conectar ao chat de voz
                    </div>

                    <footer className="mt-2 flex justify-start gap-14">
                      <Dialog.Close
                      type="button"
                      className="bg-zinc-500 px-5 h-12 rounded-md font-semibold hover:bg-zinc-600 mx-16"
                      >
                        Cancelar
                      </Dialog.Close>

                      <button 
                      type="submit"
                      className="bg-violet-500 px-4 h-12 rounded-md font-semibold flex items-center gap-3 hover:bg-violet-600 -mx-28"> 
                        <GameController size={24} />
                        Encontrar duo 
                      </button>
                    </footer>
                  </div>
                </form>
            </Dialog.Content>
          </Dialog.Portal>
        </Dialog.Root>

    </div>
  )
}

export default App
