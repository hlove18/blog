Rails.application.routes.draw do

  root to: 'posts#home'

  mount RailsAdmin::Engine => '/admin', as: 'rails_admin'

  devise_for :users
  	
	get 'about' => 'pages#about', as: :about
	get 'contact' => 'pages#contact', as: :contact

  resources :posts do
  	put 'publish' => 'posts#publish', on: :member
  	put 'unpublish' => 'posts#unpublish', on: :member
    get 'bianchini' => 'posts#bianchini', :on => :collection
    get 'love' => 'posts#love', :on => :collection
    get 'bianchini_love' => 'posts#bianchini_love', :on => :collection
	end

  resources :games do
    get 'pentris' => 'games#pentris', :on => :collection
  end

 	# For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
