class PostsController < ApplicationController
  #before_action :authenticate_user!
  before_action :set_post, only: [:show, :edit, :update, :destroy, :publish, :unpublish]

  def home
    #Line below is SLOW: loads everything from a post
    #@posts = Post.all.published.order('published_at DESC')
    #Line below is FAST: only loads the necessary elements from a post, and does not waste time loading body (body = lots of data). See post model
    @posts = Post.minimal_view.published.order('published_at DESC')
  end

  # GET /posts
  # GET /posts.json
  def index
    if user_signed_in? and current_user.admin
      #Line below is SLOW: loads everything from a post
      #@posts = Post.all.order("id")
      #Line below is FAST: only loads the necessary elements from a post, and does not waste time loading body (body = lots of data). See post model
      @posts = Post.minimal_view.order('id')
    else
      #Line below is SLOW: loads everything from a post
      #@posts = Post.all.published
      #Line below is FAST: only loads the necessary elements from a post, and does not waste time loading body (body = lots of data). See post model
      @posts = Post.minimal_view.published
    end
  end

  #personal pages:
  def bianchini
    if user_signed_in? and current_user.admin
      @posts = Post.where(:owner => 'Bianchini').minimal_view.order('id')
    else
      @posts = Post.where(:owner => 'Bianchini').minimal_view.published
    end
  end

  def love
    if user_signed_in? and current_user.admin
      @posts = Post.where(:owner => 'Love').minimal_view.order('id')
    else
      @posts = Post.where(:owner => 'Love').minimal_view.published
    end
  end

  def bianchini_love
    if user_signed_in? and current_user.admin
      @posts = Post.where(:owner => 'Bianchini-Love').minimal_view.order('id')
    else
      @posts = Post.where(:owner => 'Bianchini-Love').minimal_view.published
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
    # Active storage
    # @post.image.attach(params[:image])
    # @post.thumbnail.attach(params[:thumbnail])

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
        if saving?
          format.html { redirect_to edit_post_path(@post), notice: 'Post was successfully saved.' }
          format.json { render :edit, status: :ok, location: @post }
        else
          format.html { redirect_to @post, notice: 'Post was successfully updated.' }
          format.json { render :show, status: :ok, location: @post }
        end
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

  # Active storage delete upload.
  def delete_post_upload
    @upload = ActiveStorage::Attachment.find(params[:id])
    @upload.purge
    redirect_back(fallback_location: request.referer)
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_post
      @post = Post.friendly.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def post_params
      params.require(:post).permit(:title, :body, :description, :image, :thumbnail, :date, :owner, uploads: [])
    end

    # For "Save" button
    def saving?
      params[:commit] == "Save"
    end
end