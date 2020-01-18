class HelpersController < ApplicationController
  before_action :set_helper, only: [:show, :edit, :update, :destroy]

  # GET /helpers
  # GET /helpers.json
  def index
    @helpers = Helper.all
  end

  # GET /helpers/1
  # GET /helpers/1.json
  def show
  end

  # GET /helpers/new
  def new
    @helper = Helper.new
  end

  # GET /helpers/1/edit
  def edit
  end

  # POST /helpers
  # POST /helpers.json
  def create
    @helper = Helper.new(helper_params)

    respond_to do |format|
      if @helper.save
        format.html { redirect_to @helper, notice: 'Helper was successfully created.' }
        format.json { render :show, status: :created, location: @helper }
      else
        format.html { render :new }
        format.json { render json: @helper.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /helpers/1
  # PATCH/PUT /helpers/1.json
  def update
    respond_to do |format|
      if @helper.update(helper_params)
        format.html { redirect_to @helper, notice: 'Helper was successfully updated.' }
        format.json { render :show, status: :ok, location: @helper }
      else
        format.html { render :edit }
        format.json { render json: @helper.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /helpers/1
  # DELETE /helpers/1.json
  def destroy
    @helper.destroy
    respond_to do |format|
      format.html { redirect_to helpers_url, notice: 'Helper was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_helper
      @helper = Helper.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def helper_params
      params.require(:helper).permit(:helper_score)
    end
end
