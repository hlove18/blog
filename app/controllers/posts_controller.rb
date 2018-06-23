class PostsController < ApplicationController
  #before_action :authenticate_user!
  before_action :set_post, only: [:show, :edit, :update, :destroy, :publish, :unpublish]

  def home
    #SLOW: loads everything from a post
    #@posts = Post.all.published.order('published_at DESC')
    #FAST: only loads the necessary elements from a post, and does not waste time loading body (body = lots of data)
    @posts = Post.select("id", "title", "description", "slug", "created_at", "updated_at", "image_file_name", "thumbnail_file_name", "published", "published_at", "date").published.order('published_at DESC')
  end

  # GET /posts
  # GET /posts.json
  def index
    if user_signed_in? and current_user.admin
      #SLOW loads everything from a post
      #@posts = Post.all.order("id")
      #FAST: only loads the necessary elements from a post, and does not waste time loading body (body = lots of data)
      @posts = Post.select("id", "title", "description", "slug", "created_at", "updated_at", "image_file_name", "thumbnail_file_name", "published", "published_at", "date").order('id')
    else
      #SLOW loads everything from a post
      #@posts = Post.all.published
      #FAST: only loads the necessary elements from a post, and does not waste time loading body (body = lots of data)
      @posts = Post.select("id", "title", "description", "slug", "created_at", "updated_at", "image_file_name", "thumbnail_file_name", "published", "published_at", "date").published
    end
  end

  # GET /posts/1
  # GET /posts/1.json
  def show
    redirect_to main_app.root_path unless @post.published or (user_signed_in? and current_user.admin == true)  
  end

  # GET /posts/new
  def new
    redirect_to main_app.root_path unless user_signed_in? and current_user.admin == true
    @post = Post.new
  end

  # GET /posts/1/edit
  def edit
    redirect_to main_app.root_path unless user_signed_in? and current_user.admin == true
  end

  def publish
    @post.publish
    redirect_to posts_path
  end

  def unpublish
    @post.unpublish
    redirect_to posts_path
  end

  # POST /posts
  # POST /posts.json
  def create
    @post = Post.new(post_params)

    respond_to do |format|
      if @post.save
        format.html { redirect_to @post, notice: 'Post was successfully created.' }
        format.json { render :show, status: :created, location: @post }
      else
        format.html { render :new }
        format.json { render json: @post.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /posts/1
  # PATCH/PUT /posts/1.json
  def update
    respond_to do |format|
      if @post.update(post_params)
        format.html { redirect_to @post, notice: 'Post was successfully updated.' }
        format.json { render :show, status: :ok, location: @post }
      else
        format.html { render :edit }
        format.json { render json: @post.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /posts/1
  # DELETE /posts/1.json
  def destroy
    @post.destroy
    respond_to do |format|
      format.html { redirect_to posts_url, notice: 'Post was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_post
      @post = Post.friendly.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def post_params
      params.require(:post).permit(:title, :body, :description, :image, :thumbnail, :date)
    end
end
